## 缘起

通过 ssh 搭建简易的 git 服务时，想到了权限控制，进而想到了多用户、多文件（夹）、多用户组之间的关系能否实现。

因为一般`ls -l`都只显示文件的一个用户和一个用户组，让我想对此一探究竟。经过简单搜索，发现一个用户对多个用户组是可以实现的。

## 多用户组

### 文件视角

如果文件系统支持POSIX `ACL`扩展，就可以支持多个用户组。大部分 unix 工具和应用仅显示 `user:group:other` 这三种名称和对应权限。

1. 读取ACL设置：`getfacl <file/dir>`
2. 改变ACL设置：`setfacl`

更多请阅读：[ACL: Using Access Control Lists on Linux](http://bencane.com/2012/05/27/acl-using-access-control-lists-on-linux/)

### 用户视角

可为单个用户添加额外的用户组

    usermod -a -G <group1>,<group2>,<group3> <username>

### 关系

    用户 <--> 用户组（代表着权限） <--> 文件（夹）

所以要控制权限，必须为文件增加额外的用户组，这些用户组实质上代表的是各种`rwx`权限，同时也要修改用户属性，把他们添加到各种用户组中。

这个 git 仓库实例中，其实只设置一个 primary 用户组也行，然后设置项目裸仓库根文件夹的权限为 775 即可。意即所有者（管理员）和项目同名用户组拥有读写权限，而其他人则只拥有读取权限，同时因为文件夹必须有执行权限才能列出目录下的文件，都加上了执行权限。

## 用户组操作

新增用户组

    groupadd <groupname>

更改基础用户组

    usermod -g <groupname> username

查看用户组

    groups [<username>]
    id <username>

新增用户并赋给用户组

    useradd [-g <primary group name/id> -G <supplementary groups list> -p <password> -d <home> -s <shell>] username

更改用户密码

    passwd <username>

## 用户操作

    useradd
    usermod
    userdel

## Links

- [Setup your own Git Server over SSH](http://crosbymichael.com/setup-your-own-git-server-over-ssh.html)
- [Git - Getting Git on a Server](https://git-scm.com/book/en/v2/Git-on-the-Server-Getting-Git-on-a-Server)
- [Can a directory belong to more than one group?](http://askubuntu.com/questions/143675/can-a-directory-belong-to-more-than-one-group)
- [How do I add a user to multiple groups in Ubuntu?](http://superuser.com/questions/95972/how-do-i-add-a-user-to-multiple-groups-in-ubuntu)
- [Add a User to a Group (or Second Group) on Linux](http://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/)