## Install sentry step by step

```shell
docker run -d --name sentry-redis redis
docker run -d --name sentry-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=sentry postgres

export SENTRY_SECRET_KEY=$(docker run --rm sentry config generate-secret-key) && echo $SENTRY_SECRET_KEY | tee secret-key

docker run -it --rm -e SENTRY_SECRET_KEY=${SENTRY_SECRET_KEY} --link sentry-postgres:postgres --link sentry-redis:redis sentry upgrade
docker run -d --name my-sentry -p 9000:9000 -e SENTRY_SECRET_KEY=${SENTRY_SECRET_KEY} --link sentry-redis:redis --link sentry-postgres:postgres sentry

docker run -d --name sentry-cron -e SENTRY_SECRET_KEY=${SENTRY_SECRET_KEY} --link sentry-postgres:postgres --link sentry-redis:redis sentry run cron
docker run -d --name sentry-worker-1 -e SENTRY_SECRET_KEY=${SENTRY_SECRET_KEY} --link sentry-postgres:postgres --link sentry-redis:redis sentry run worker
```

更多自定义：https://hub.docker.com/_/sentry/
