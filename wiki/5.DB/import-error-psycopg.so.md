我写了一个网站，用的是 SQLalchemy + Postgresql。在部署的时候，出现如下错误：

	ImportError: /usr/local/lib/python3.4/site-packages/psycopg2/_psycopg.cpython-34m.so: undefined symbol: lo_truncate64

通过如下操作修复：

```txt
$ ll /usr/lib |grep libpq
lrwxrwxrwx  1 root root   12 May 27 08:46 libpq.so.5 -> libpq.so.5.4
-rw-r--r--  1 root root 183K May 27 08:46 libpq.so.5.4

$ ll /usr/local/pgsql/lib/ | grep libpq
-rw-r--r-- 1 root staff 273K Jun  4 13:23 libpq.a
lrwxrwxrwx 1 root staff   12 Jun  4 13:23 libpq.so -> libpq.so.5.8*
lrwxrwxrwx 1 root staff   12 Jun  4 13:23 libpq.so.5 -> libpq.so.5.8*
-rwxr-xr-x 1 root staff 183K Jun  4 13:23 libpq.so.5.8*
-rwxr-xr-x 1 root staff  18K Jun  4 13:23 libpqwalreceiver.so*

$ rm -rf /usr/lib/libpq.so.5
$ ln -s /usr/local/pgsql/lib/libpq.so.5.8 /usr/lib/libpq.so.5
```

其中`ll`是我对`ls -alFh`作的映射，通过在`~/.bash_aliases`添加如下一行即可：

	alias ll='ls -alFh'

## 参考链接

- http://www.leeladharan.com/importerror-psycopg-so:-undefined-symbol:-lo-truncate64