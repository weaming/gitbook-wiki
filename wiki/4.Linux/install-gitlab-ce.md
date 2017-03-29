## Gitlab CE（社区版）安装

- 安装过程：https://about.gitlab.com/downloads/
- 安装硬件需求：http://doc.gitlab.com/ce/install/requirements.html
- 其他安装方式：https://about.gitlab.com/installation/


## Debian

https://about.gitlab.com/downloads/#debian8

#### 1.Install and configure the necessary dependencies

    sudo apt-get install curl openssh-server ca-certificates postfix

#### 2.Add the GitLab package server and install the package

    curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
    sudo apt-get install gitlab-ce

If you are not comfortable installing the repository through a piped script, you can find the [entire script](https://packages.gitlab.com/gitlab/gitlab-ce/install) here and select and [download the package manually](https://packages.gitlab.com/gitlab/gitlab-ce) and install using

    curl -LJO https://packages.gitlab.com/gitlab/gitlab-ce/packages/debian/jessie/gitlab-ce-XXX.deb/download
    dpkg -i gitlab-ce-XXX.deb

在这一步，因为本地通过`apt-get`安装下载速度很慢，我采用了deb包安装的方式，安装过程有点长，用了几分钟。在上面[download the package manually](https://packages.gitlab.com/gitlab/gitlab-ce)下载[debian8的安装包](https://packages-gitlab-com.s3.amazonaws.com/7/8/debian/package_files/5200.deb?AWSAccessKeyId=AKIAJ74R7IHMTQVGFCEA&Signature=M77omNT9rsYXlCrpgHXbDhrPqdo%3D&Expires=1466754911)（注意：以`.deb`结尾的链接，并不是下载链接，需在这个页面里点击 Download 下载按钮下载）。安装过程记录见后文。

可选方案是使用清华大学的gitlab镜像源：If you are located in China, try using https://mirror.tuna.tsinghua.edu.cn/help/gitlab-ce/

#### 3.Configure and start GitLab

编辑`/etc/gitlab/gitlab.rb`这个文件进行配置。我更改了外网访问域名后，在hosts里指向本机`198.162`开头的局域网IP，然后公司团队即可访问。

    sudo gitlab-ctl reconfigure

#### 4.Browse to the hostname and login

On your first visit, you'll be redirected to a password reset screen to provide the password for the initial administrator account. Enter your desired password and you'll be redirected back to the login screen.

The default account's username is root. Provide the password you created earlier and login. After login you can change the username if you wish.


### 手动安装

```
02:49 weaming@debian:~/Downloads
$ ls
github  gitlab-ce_8.9.0-ce.0_amd64.deb  vmware-tools-distrib

02:50 weaming@debian:~/Downloads
$ sudo dpkg -i gitlab-ce_8.9.0-ce.0_amd64.deb
[sudo] password for weaming:
Selecting previously unselected package gitlab-ce.
(Reading database ... 150590 files and directories currently installed.)
Preparing to unpack gitlab-ce_8.9.0-ce.0_amd64.deb ...
Unpacking gitlab-ce (8.9.0-ce.0) ...
Setting up gitlab-ce (8.9.0-ce.0) ...
gitlab: Thank you for installing GitLab!
gitlab: To configure and start GitLab, RUN THE FOLLOWING COMMAND:

sudo gitlab-ctl reconfigure

gitlab: GitLab should be reachable at http://debian.bitsflow.org
gitlab: Otherwise configure GitLab for your system by editing /etc/gitlab/gitlab.rb file
gitlab: And running reconfigure again.
gitlab:
gitlab: For a comprehensive list of configuration options please see the Omnibus GitLab readme
gitlab: https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/README.md
gitlab:
It looks like GitLab has not been configured yet; skipping the upgrade script.
```