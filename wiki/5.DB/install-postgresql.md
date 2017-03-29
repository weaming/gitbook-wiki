## 源码下载

http://www.postgresql.org/ftp/source/

## Plugins

- postgresql-client
 - client libraries and client binaries
- postgresql
 - core database server
- postgresql-contrib
 - additional supplied modules
- libpq-dev
 - libraries and headers for C language frontend development
- postgresql-server-dev
 - libraries and headers for C language backend development
- pgadmin3
 - pgAdmin III graphical administration utility

## 简洁版本

`gmake`可替换为`make`

```
./configure
gmake
su
gmake install
adduser postgres
mkdir /usr/local/pgsql/data
chown postgres /usr/local/pgsql/data
su - postgres
/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
/usr/local/pgsql/bin/postgres -D /usr/local/pgsql/data >logfile 2>&1 &
/usr/local/pgsql/bin/createdb test
/usr/local/pgsql/bin/psql test
```

## 更多

[postgresql 入门](/note/postgresql-quickstart/)

## 参考

- [Installation from Source Code](http://www.postgresql.org/docs/9.0/static/installation.html)
- [PostgreSQL: Linux downloads (Debian)](http://www.postgresql.org/download/linux/debian/)
- [Short Version](http://www.postgresql.org/docs/9.0/static/install-short.html)