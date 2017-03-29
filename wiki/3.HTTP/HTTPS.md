![](http://neilimg.b0.upaiyun.com/flow/https.jpg)

SSL安全等级测试 测试地址[https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)
---
测试结果

![](http://neilimg.b0.upaiyun.com/flow/https-c.png)

SSLv3(TLSv1.3)不安全
---
在Nginx中禁用
```
ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
```

logjam
---
[Logjam: PFS Deployment Guide](https://weakdh.org/sysadmin.html)

Create some dhparam entropy:

```
openssl dhparam -out dhparams.pem 2048
```

To be placed in the website configuration server block in /etc/nginx/sites-enabled/default :
```
ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';
ssl_prefer_server_ciphers on;
```

DH parameters
```
ssl_dhparam {path to dhparams.pem}
```

This site works only in browsers with SNI support.
---
### SNI 是什么 （参考：[This site works only in browsers with SNI support – 木瓜园](https://muguayuan.com/2015/2863.html)）

简单来说 SNI 是 TLS 的一个功能扩展，有了 SNI 就可以在单个 IP 上启用多个 SSL 证书，现实一点说就是可以在只有一个 IP 地址的 VPS 上建立两个或更多的 https 网站了。

### 检测 nginx 是否启用 SNI
```
$ nginx -V
nginx version: nginx/1.4.7
built by gcc 4.7.2 (Debian 4.7.2-5)
TLS SNI support enabled
```

>Server Name Indication (SNI) is an extension to the TLS computer networking protocol by which a client indicates which hostname it is attempting to connect to at the start of the handshaking process. This allows a server to present multiple certificates on the same IP address and TCP port number and hence allows multiple secure (HTTPS) websites (or any other Service over TLS) to be served off the same IP address without requiring all those sites to use the same certificate. It is the conceptual equivalent to HTTP/1.1 name-based virtual hosting, but for HTTPS. The desired hostname is not encrypted, so an eavesdropper can see which site is being requested.
>
>To make SNI useful, as with any protocol, the vast majority of visitors must use web browsers that implement it. **Users whose browsers do not implement SNI are presented with a default certificate and hence are likely to receive certificate warnings.**

因此只要在客户端请求时，如果没有指明域名，那么就返回一个默认证书。

[How to define which SSL certificate nginx sends first with SNI?](http://serverfault.com/questions/488427/how-to-define-which-ssl-certificate-nginx-sends-first-with-sni)

The `default_server` setting of the `listen` directive should determine which certificate is sent for a request without SNI set in the handshake. Change the `listen` directive of the desired default:

```
listen 443 default_server ssl;
```

结果
---
还没有获得A+

![](http://neilimg.b0.upaiyun.com/flow/https-A.png)

开启了HSTS
---

![](http://neilimg.b0.upaiyun.com/flow/A%2B.png)