# 部署 Gogs Git服务

## 安装
二进制下载安装，数据库采用的是Postgresql，前端采用Nginx作为反向代理，同时采用`supervisor`管理程序运行

## Nginx

### ~~没有正常代理 HTTP 基本认证相关的请求、响应头~~

虽然Gogs文档没有提到这一点（好像之前不做特别设置也可以啊，暂且记录下来吧）

```
server {
    listen 80;
    server_name git.exmaple.com;
    # 这里是设置POST请求体大小为无限制，有时git提交的POST请求体会很大
    # 也可以设置为比如 512m 这样一个具体值
    # Set chunks to unlimited, as the body's can be huge
    client_max_body_size 0;

    location / {
        proxy_pass http://localhost:4000;

        proxy_redirect     off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP  $remote_addr;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Forwarded-Proto $scheme;

        # 这里就是设置设置代理http基本认证的指令
        proxy_set_header Authorization $http_authorization;
        proxy_pass_header  Authorization;
    }
}
```

### git 通过 http 提交的时候报错

报错内容：`fatal: The remote end hung up unexpectedly`

搜了很久才搜到能解决的[方案](https://confluence.atlassian.com/stashkb/error-rpc-failed-result-22-push-to-stash-fails-604537633.html)

Increase the Git buffer size to the largest individual file size of your repo:

    git config --global http.postBuffer 157286400

- When pushing a large amount of data (initial push of a big repository, change with very big file(s)) may require a higher http.postBuffer setting on your git client (not the server). From https://www.kernel.org/pub/software/scm/git/docs/git-config.html

>http.postBuffer
>Maximum size in bytes of the buffer used by smart HTTP transports when POSTing data to the remote system. For requests larger than this buffer size, HTTP/1.1 and Transfer-Encoding: chunked is used to avoid creating a massive pack file locally. Default is 1 MiB, which is sufficient for most requests.
- Configuration on your reverse proxy. Usually ngnix the parameter `client_max_body_size` is a blocker. The reverse proxy may also have a connection timeout that's closing the connection (e.g. TimeOut or ProxyTimeout in apache, `proxy_read_timeout` in ngnix). Try bypassing the proxy by pushing directly to Stash IP:port. If this works, it's highly likely that the proxy server is causing the early disconnect and needs to be tuned.

### Gogs 配置

[传送门](https://gogs.io/docs/advanced/configuration_cheat_sheet)

我自己改动了的一些关键设置：

```
[repository]
ROOT                      = /home/git/

[server]
PROTOCOL               = http
DOMAIN                 = git.r-pac.com.hk
ROOT_URL               = http://git.r-pac.com.hk/
HTTP_ADDR              = 0.0.0.0
HTTP_PORT              = 4000

; Disable SSH feature when not available
DISABLE_SSH            = false
; Whether use builtin SSH server or not.
START_SSH_SERVER       = false
; Domain name to be exposed in clone URL
SSH_DOMAIN             = %(DOMAIN)s
; Network interface builtin SSH server listens on
SSH_LISTEN_HOST        = 0.0.0.0
; Port number to be exposed in clone URL
SSH_PORT               = 22
; Port number builtin SSH server listens on
SSH_LISTEN_PORT        = %(SSH_PORT)s
; Root path of SSH directory, default is '~/.ssh', but you have to use '/home/git/.ssh'.
SSH_ROOT_PATH          = /home/git/.ssh

; Disable CDN even in "prod" mode
OFFLINE_MODE           = true
```

其中，使用ssh协议的时候，会在 git 用户的 HOME 目录寻找仓库文件

    sudo usermod -d /home/git/ git

添加的 ssh 公钥会添加到 git 用户的 `~git/.ssh/authorized_keys` 文件中，所以必须具有写权限

    sudo chown -R git:git /home/git
    sudo chmod +x /home/git/.ssh
    sudo chmod +rw /home/git/.ssh/authorized_keys

如果 ROOT 设置不与 git 用户的 HOME 目录相同，貌似这两个地方的仓库文件是通过硬链接共享底层的存储空间的，
因为我在迁移`cp`的过程中，系统提示那些repos的文件夹是同一“文件”

### SSH commit 成功，但是web端不显示更新


可能原因：
- 在使用 SSH 推送时，Gogs 依赖通过执行钩子脚本（Hook Script）来更新仓库和最近活动。
- Update 钩子指向错误的二进制路径

解决方案：到管理员控制面板（/admin）执行以下操作：

- 重新同步所有仓库的 pre-receive、update 和 post-receive 钩子
