安装
---
```
sudo apt-get install postgresql-client # 安装客户端
sudo apt-get install postgresql # 安装服务端
sudo apt-get install pgadmin3 # 安装图形界面管理
```

linux用户、pg用户、数据库
----
注意区分这三个名称

添加新用户和新数据库
---
初次安装后，默认添加一个名为postgres数据库，一个名为postgres的数据库管理员用户，同时生成了一个名为postgres的Linux用户。

**方法一，用postgresql控制台**

```
sudo adduser dbuser # 添加linux用户
sudo su - postgres # 切换到postgres这个linux用户（`-`表示连同用户环境变量都切换过去），切换时需要输入linux用户密码
pssql # 在linux用户postgres用户下登录pgsql控制台，登录的是与linux用户名同名的数据库
```

**控制台下命令：**

普通用户登陆后显示
```
psql (9.3.10)
Type "help" for help.

exampledb=>
```
如果是管理员用户，则是`dbname=#`

```
\password 数据库用户名 # 修改数据库用户的密码。以\开头的命令结尾不需要加分号";"
CREATE USER dbuser WITH PASSWORD 'password'; # 创建数据库用户，并初始化密码
CREATE DATABASE mydb OWNER dbuser; # 创建数据库，并指定所有者
GRANT ALL PRIVILEGES ON DATABASE mydb to dbuser; # 将mydb数据库所有权限都赋予数据库用户dbuser，否则dbuser只有登录权限。
\q # 退出控制台。也可以用ctrl+d.
```

**方法二，使用shell命令**

```
sudo -u postgres createuser --superuser dbuser # 使用linux用户postgres来新建超级用户dbuser
sudo -u postgres psql # 使用linux用户postgres登录与linux用户同名的数据库
# 修改 dbuser 密码参考方法一
```

登录数据库
---
一个普通的登录命令：
```
psql -U dbuser -d mydb -h 127.0.0.1 -p 5432
```
其中

- U 数据库用户名，如果当前linux用户名与数据库用户名相同，则可省略
- d 数据库名，如果登录用户名与数据库名相同，则可省略
- h 主机地址，如果使用“localhsot”则需要输入密码，如果没有添加 -U 参数，可以省略
- p 端口，默认5432

恢复外部数据
```
psql mydb < mydb.sql
```

pgsql的实用shell命令
---
```
psql # 一个基于命令行的PostgreSQL交互式客户端程序
createdb # 创建一个新的PostgreSQL的数据库（和SQL语句：CREATE DATABASE 相同）
createuser # 创建一个新的PostgreSQL的用户（和SQL语句：CREATE USER 相同）
dropdb # 删除数据库
dropuser # 删除用户
pg_dump # 将PostgreSQL数据库导出到一个脚本文件
pg_dumpall # 将所有的PostgreSQL数据库导出到一个脚本文件
pg_restore # 从一个由pg_dump或pg_dumpall程序导出的脚本文件中恢复PostgreSQL数据库
vacuumdb # 清理 和分析一个PostgreSQL数据库，它是客户端程序psql环境下SQL语句VACUUM的shell脚本封装，二者功能完全相同
```

pgsql控制台中一些命令
---
```
\l # 列出现存数据库
\q # 退出psql
\c # 从当前数据库转到新数据库，后接新数据库名。相当于mysql中的“use dbname”
\dt # 显示表
\d tname # 显示表结构，不加表名则和`\dt`相同
\di # 显示索引
!psql -U weaming -d dbname # 感叹号！加命令，相当于在shell下执行命令

create group # 创建用户组
alter group gname add user uname1,uname2,...; # 添加用户到用户组，gname用户组名，uname用户名
create databse
drop databse
alter table tname1 rename to tname2; # 重命名表
drop talbe tname; # 删除表

# 表内操作
ALTER TABLE tname ADD COLUMN cname ctype; 添加字段。cname字段名，ctype字段类型。
alter table tname drop column cname; 删除字段
alter table tname rename column cname1 to cname2; 重命名字段
alter talbe tname alter column cname set default dvalue; 设置字段默认值。dvalue默认值。
insert into tname (cname1,cname2,...) values (cvalue1,cvalue2,...); 插入数据
update tname set cname=cvalue where rcondition; 修改数据。rcondition行条件。
delete from tname where rcondition; 删除数据
delete from tname; 删除整个表
```

pgsql用户认证
---
PostgreSQL数据目录中的`pg_hba.conf`的作用就是用户认证。
我的ubuntu14.04上，此配置文件在目录`/etc/postgresql/9.3/main/`

(1)允许在本机上的任何身份连接任何数据库
```
TYPE DATABASE USER IP-ADDRESS IP-MASK METHOD

local all all trust(无条件进行连接)
```
(2)允许IP地址为192.168.1.x的任何主机与数据库sales连接
```
TYPE DATABASE USER IP-ADDRESS IP-MASK METHOD

host sales all 192.168.1.0 255.255.255.0 ident sameuser(表明任何操作系统用户都能够以同名数据库用户进行连接)
```