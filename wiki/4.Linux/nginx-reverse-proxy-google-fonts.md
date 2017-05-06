# 自己反代Google字体库，实现国内/外均高速访问

未经测试。来源：[自己反代Google字体库，实现国内/外均高速访问](http://hjc.im/google-fonts-reverse-proxy/)

```
upstream googleapis {
    server fonts.googleapis.com:80;
}

upstream gstatic {
    server fonts.gstatic.com:80;
}

server {
    listen 80;
    listen [::]:80;

    server_name fonts.ligstd.com;#改为自己的字体库域名，fonts.xxxxxx.com
    valid_referers server_name *.ligstd.com ligstd.com *.hjc.im hjc.im; # 限制引用的域名。改成自己需要用到字体库的网站域名的即可。如果你想要做公益服务，可以将此行和下方的#if ($invalid_referer) {...}去掉。
    if ($invalid_referer) {
        return 404;
    }

    location /css {
        sub_filter 'fonts.gstatic.com' 'fonts.ligstd.com';#将fonts.ligstd.com改为自己的字体库域名。
        sub_filter_once off;
        sub_filter_types text/css;
        proxy_pass_header Server;
        proxy_set_header Host fonts.googleapis.com;
        proxy_set_header Accept-Encoding '';
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_pass http://googleapis;
    }

    location / {
        proxy_pass_header Server;
        proxy_set_header Host fonts.gstatic.com;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_pass http://gstatic;
    }
}

#下方为HTTPS设置，如果只需要HTTP访问，从这里开始往下的内容就不需要看了。
server {
    listen 106.186.18.133:443 ssl spdy; #将这一行改为"自己的IP地址:443"
    listen [2400:8900::f03c:91ff:fe73:bc8f]:443 ssl spdy;#将这一行改为"[自己的IPv6地址]:443"，没有IPv6可以不填。
    ssl on;
    ssl_certificate /root/fonts.ligstd.com/ssl.crt; #改为自己的SSL证书位置
    ssl_certificate_key /root/fonts.ligstd.com/ssl.key; #改为自己的SSL私钥位置
    ssl_session_timeout 5m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers ECDH+AESGCM:ECDH+AES256:ECDH+AES128:DH+3DES:RSA+3DES:!ADH:!AECDH:!MD5;
    #上面几行视情况而定，可以去掉ssl_ciphers和ssl_prefer_server_ciphers两行。
    server_name fonts.ligstd.com;#改为自己的字体库域名

    valid_referers server_name *.ligstd.com ligstd.com *.hjc.im hjc.im;#同样，改为自己需要使用字体库的网站域名。公益服务去掉这几行。
    if ($invalid_referer) {
        return 404;
    }

    location /css {
        sub_filter 'http://fonts.gstatic.com' 'https://fonts.ligstd.com'; #将fonts.ligstd.com改为字体库域名，但是https千万别改。
        sub_filter_once off;
        sub_filter_types text/css;
        proxy_pass_header Server;
        proxy_set_header Host fonts.googleapis.com;
        proxy_set_header Accept-Encoding '';
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_pass http://googleapis;
    }

    location / {
        proxy_pass_header Server;
        proxy_set_header Host fonts.gstatic.com;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_pass http://gstatic;
    }
}
```