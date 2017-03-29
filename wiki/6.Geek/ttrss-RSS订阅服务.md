openshift搭建Tiny Tiny RSS服务 [官方教程](https://tt-rss.org/gitlab/fox/tt-rss/wikis/InstallationNotes)
==
编写了安装脚本和相关配置文件：[backupvps/ttrss](https://github.com/weaming/backupvps/tree/master/ttrss)

- 小众软件：http://www.appinn.com/tiny-tiny-rss
- Wjchen博客：https://wjchen.me/index.php/ttrss-1.html
- openshift：https://www.openshift.com
  - openshift自动部署脚本：https://hub.openshift.com/quickstarts/7-tiny-tiny-rss
- 初始用户名：admin；密码：password
- 可在openshift更改域名

主题等

- reeder主题css：https://github.com/tschinz/tt-rss_reeder_theme
- TinyTinyRSS Fever API plugin：https://github.com/dasmurphy/tinytinyrss-fever-plugin
- ttrss-mobile：https://github.com/mboinet/ttrss-mobile
- g2ttrss-mobile：https://github.com/g2ttrss/g2ttrss-mobile

[DigitalOcean搭建ttrss (Debian7x64)](https://www.digitalocean.com/community/tutorials/how-to-install-ttrss-with-nginx-for-debian-7-on-a-vps)
--

```
sudo apt-get update
sudo apt-get install php5 php5-pgsql php5-fpm php-apc php5-curl php5-cli -y
sudo apt-get install postgresql -y
```

建数据库

```
sudo -u postgres psql
postgres=# CREATE USER "www-data" WITH PASSWORD 'yourpasshere';
postgres=# CREATE DATABASE ttrss WITH OWNER "www-data";
postgres=# \quit
```

安装Nginx

```
sudo apt-get install nginx -y
sudo service nginx start
```

安装ttrss

```
wget https://tt-rss.org/gitlab/fox/tt-rss/repository/archive.zip
unzip archive.zip
sudo rm archive.zip
sudo mv tt-rss* /usr/share/nginx/ttrss
sudo chown -R www-data:www-data ttrss
```

## 配置Nginx

```
sudo vim /etc/nginx/sites-available/ttrss
```

文件内容：

```
server {
    listen  80; ## listen for ipv4; this line is default and implied

    root /usr/share/nginx/ttrss; ##配置站点文件目录
    index index.html index.htm index.php;

    access_log /var/log/nginx/ttrss_access.log;
    error_log /var/log/nginx/ttrss_error.log info;

    server_name your.domain.here;

    location / {
        index           index.php;
    }

    location ~ \.php$ {
        try_files $uri = 404; #Prevents autofixing of path which could be used for exploit
        fastcgi_pass unix:/var/run/php5-fpm.sock;
        fastcgi_index index.php;
        include /etc/nginx/fastcgi_params;
    }

}
```

使配置生效，并删除默认欢迎页面，并重启Nginx

```
cd /etc/nginx/sites-enabled;sudo rm default;sudo ln -s ../sites-available/ttrss ttrss;sudo service nginx restart
```

安装feedly主题：

```
cd /usr/share/nginx/ttrss/themes;
wget https://github.com/levito/tt-rss-feedly-theme/archive/master.zip;unzip master.zip;rm master.zip;cd tt-rss-feedly-theme-master;
rm -rf feedly-screenshots README.md;
chmod 755 -R *;
chown www-data:www-data *
mv ./* ../
cd ..
rm -rf tt-rss-feedly-theme-master
```

自动更新Feed

```
sudo vim /etc/crontab
倒数第二行（#号前一行）添加：
*/30 * * * * www-data /usr/bin/php /usr/share/nginx/ttrss/update.php --feeds --quiet
```

crontab

```
1. 确认crontab是否安装：
执行 crontab 命令如果报 command not found，就表明没有安装
2. 安装 crontab
执行 yum install -y vixie-cron
3. 确认是否安装成功:
执行 crontab -l
4. 看是否设置了开机自动启动
chkconfig --list crond
5. 启动crontab
service crond start
```

访问你的域名或IP(会跳转到`/install/`)
---
**后期碰到的问题：** [nginx上，http状态200响应，PHP空白返回的问题](http://www.cnxct.com/php-return-empty-result-on-nginx-without-script_filename/)

Nginx中location添加：

```
fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
```

页面中填写：

```
Database type: Select PostgreSQL
Username: www-data
Password: 你创建的数据库密码
Database Name: ttrss
Hostname: leave blank
Port: 5432
```

## Postgresql 修改密码

    alter user postgres with password 'foobar';

