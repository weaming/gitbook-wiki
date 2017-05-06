# 反代理其他网站

代理同时，对HTML中的资源引用来源作替换。

```
 server {
        listen 80;
        listen 443 ssl http2;
        server_name article.bitsflow.org;
        ssl_certificate /keys/article.bitsflow.org.crt;
        ssl_certificate_key /keys/article.bitsflow.org.key;

        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
        }

        location / {
            sub_filter 'https://botanwang.com' 'https://article.bitsflow.org';
            sub_filter_once off;
            sub_filter_types *;
            proxy_pass https://botanwang.com;
            proxy_set_header Accept-Encoding "";
        }
    }
```

## 参考链接
- [Module ngx_http_sub_module](http://nginx.org/en/docs/http/ngx_http_sub_module.html)
- [nginx替换网站响应内容（ngx_http_sub_module）](http://www.ttlsa.com/linux/nginx-modules-ngx_http_sub_module/)
- [sub_filter 由于 gzip 不能插入内容](http://www.nginx.cn/829.html)