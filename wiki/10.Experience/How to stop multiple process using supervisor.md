### Question: supervisord can't stop `uwsgi` using multiple processes

Actually, I found have to do like this:

/etc/supervisor/conf.d/app.conf
```
stopsignail = QUIT
```
The default signal of supervisor is `SIGTERM`, see [supervisor doc](http://supervisord.org/configuration.html#program-x-section-settings)

/etc/uwsgi/app.ini
```
processes = 4
master = true
```

Must set `--master` when start uwsgi, and supervisor can stop these processed correctly.

- See [this answer](http://stackoverflow.com/a/38362251/5281824)
- Signals wiki https://en.wikipedia.org/wiki/Unix_signal
