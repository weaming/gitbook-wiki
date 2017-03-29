Failed operation record
---
```
cd lnmp1.2-full/src/php-5.6.9/ext
yum install postgresql postgresql-devel
./configure --with-php-config=/usr/local/php/bin/php-config --with-pgsql
make && make install
```

初始化postgresql
---
参考：[Linux postgresql 安装配置详解«海底苍鹰(tank)博客](http://blog.51yip.com/pgsql/1520.html)

```
$ mkdir -p /var/lib/pgsql/data
$ cd /var/lib/pgsql
$ chown postgres.postgres data
$ su  postgres
bash-4.2$ initdb -E UTF-8 -D /var/lib/pgsql/data --locale=en_US.UTF-8 -U postgres -W
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.UTF-8".
The default text search configuration will be set to "english".

fixing permissions on existing directory /var/lib/pgsql/data ... ok
creating subdirectories ... ok
selecting default max_connections ... 100
selecting default shared_buffers ... 32MB
creating configuration files ... ok
creating template1 database in /var/lib/pgsql/data/base/1 ... ok
initializing pg_authid ... ok
Enter new superuser password:
Enter it again:
setting password ... ok
initializing dependencies ... ok
creating system views ... ok
loading system objects' descriptions ... ok
creating collations ... ok
creating conversions ... ok
creating dictionaries ... ok
setting privileges on built-in objects ... ok
creating information schema ... ok
loading PL/pgSQL server-side language ... ok
vacuuming database template1 ... ok
copying template1 to template0 ... ok
copying template1 to postgres ... ok

WARNING: enabling "trust" authentication for local connections
You can change this by editing pg_hba.conf or using the option -A, or
--auth-local and --auth-host, the next time you run initdb.

Success. You can now start the database server using:

    postgres -D /var/lib/pgsql/data
or
    pg_ctl -D /var/lib/pgsql/data -l logfile start
```