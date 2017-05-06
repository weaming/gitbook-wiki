# PostgreSQL Q&A
## Reset blank table's ID sequence to make it start from 1

[Reset PostgreSQL primary key to 1 - Stack Overflow](http://stackoverflow.com/questions/3819292/reset-postgresql-primary-key-to-1)

    ALTER SEQUENCE <tablename>_<id>_seq RESTART WITH 1

Check current next id:

    select nextval('<tablename>_<id>_seq')

## How to change databse maximum number of concurrent connections

`max_connections` sets exactly that: the maximum number of client connections allowed. This is very important to some of the below parameters (particularly `work_mem`) because there are some memory resources that are or can be allocated on a per-client basis, so the maximum number of clients suggests the maximum possible memory use. Generally, PostgreSQL on good hardware can support a few hundred connections. If you want to have thousands instead, you should consider using connection pooling software to reduce the connection overhead.

**Query settting**

    select * from pg_settings;

`alter system ...`: https://www.postgresql.org/docs/current/static/sql-altersystem.html

**When they take effect**

PostgreSQL settings have different levels of flexibility for when they can be changed, usually related to internal code restrictions. The complete list of levels is:

- Postmaster: requires restart of server
- Sighup: requires a HUP of the server, either by kill -HUP (usually -1), `pg_ctl reload`, or `SELECT pg_reload_conf()`;
- User: can be set within individual sessions, take effect only within that session
- Internal: set at compile time, can't be changed, mainly for reference
- Backend: settings which must be set before session start
- Superuser: can be set at runtime for the server by superusers

Most of the time you'll only use the first of these, but the second can be useful if you have a server you don't want to take down, while the user session settings can be helpful for some special situations. You can tell which type of parameter a setting is by looking at the "context" field in the `pg_settings` view.

Note: `max_connections`'s `context` level is `postmaster`, so take effect after changed it need restart server.

See [Tuning Your PostgreSQL Server](https://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server) for more.

## How to restart postgreSQL server

[PostgreSQL: Documentation: 9.1: pg_ctl](https://www.postgresql.org/docs/9.1/static/app-pg-ctl.html)

## How to reload setttings

    pg_ctl reload -D <data_directory>
    SELECT pg_reload_conf();

## How to list all connections

Use

    SELECT * FROM pg_stat_activity;

to get process IDs. Now cancel all active queries on a connection:

    SELECT pg_cancel_backend(procid)

This does not terminate the connection itself, though.

 Kill the connection:

    SELECT pg_terminate_backend(procid)

If you have not canceled the queries on the connection, they are all rudely termi‐ nated now. You can kill multiple connections by wrapping them in a `SELECT`.

    SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE usename = 'some_role';
