```
user www-data;
worker_processes 4;
pid /var/run/nginx.pid;
daemon off;
#master_process off;

events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    types_hash_max_size 2048;
    gzip on;
    gzip_disable "msie6";

    #include /etc/nginx/conf.d/*.conf;
    #include /etc/nginx/sites-enabled/*;

    #access_log /var/log/nginx/access.log;
    #error_log /var/log/nginx/error.log;

    # SSL
    #add_header Content-Security-Policy "upgrade-insecure-requests";
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
    ssl_prefer_server_ciphers on;

    #ssl_ciphers 'AES128+EECDH:AES128+EDH';
    ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';
    ssl_dhparam /www/dhparams.pem;

    keepalive_timeout  65;

    server {
        listen 80;
        listen 443 ssl default_server;
        ssl_certificate /keys/wowapi.org.crt;
        ssl_certificate_key /keys/wowapi.org.key;
        add_header Strict-Transport-Security "max-age=16070400; includeSubDomains; preload";
        add_header Content-Security-Policy "upgrade-insecure-requests";

        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
        }

        server_name wowapi.org;

        access_log /var/log/nginx/access-blog.log;
        error_log /var/log/nginx/error-blog.log;

        location ~.*\.(js|css|woff2)?$  {
            expires 7d;
            root /www/blogger/public;
        }

        location / {
            root /www/blogger/public;
        }

    }

    server {
        listen 80;
        listen 443;
        ssl on;
        ssl_certificate /keys/ruanjiadeng.com.crt;
        ssl_certificate_key /keys/ruanjiadeng.com.key;

        root /usr/share/nginx/ttrss;
        index index.html index.htm index.php;

        server_name rss.ruanjiadeng.com;

        location / {
        index           index.php;
        }

        location ~ \.php$ {
        try_files $uri = 404;
        fastcgi_pass unix:/tmp/php-cgi.sock;
        fastcgi_index index.php;
        include /etc/nginx/fastcgi_params;
        }

    }

    server {
        server_name gg.ruanjiadeng.com;
        listen 80;
        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
        }
        listen 443;
        ssl on;
        ssl_certificate /keys/gg.ruanjiadeng.com.crt;
        ssl_certificate_key /keys/gg.ruanjiadeng.com.key;

        resolver 8.8.8.8;
        location / {
        google on;
        google_scholar on;
        }
    }

    server {
        server_name myss.ml;
        listen 80;

        resolver 8.8.8.8;
        location / {
        google on;
        google_scholar on;
        }
    }

    server {
        server_name nav.ruanjiadeng.com;
        listen 80;
        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
        }
        listen 443;
        ssl on;
        ssl_certificate /keys/ruanjiadeng.com.crt;
        ssl_certificate_key /keys/ruanjiadeng.com.key;

        location / {
        proxy_pass http://127.0.0.1:9000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }

    server {
        server_name docs.ruanjiadeng.com;
        listen 80;
        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
        }
        listen 443;
        ssl on;
        ssl_certificate /keys/ruanjiadeng.com.crt;
        ssl_certificate_key /keys/ruanjiadeng.com.key;

        access_log /var/log/nginx/access-docs.log;
        error_log /var/log/nginx/error-docs.log;

        location / {
            root /root/github/idocs/;
            expires 14d;
        }
    }

    server {
        server_name file.ruanjiadeng.com;
        listen 80;

        location / {
            root /dload/;
            autoindex on;
            autoindex_localtime on;
            autoindex_exact_size off;
            expires 1h;
        }
    }

    server {
        server_name weixin.ruanjiadeng.com;
        listen 80;

        location / {
        proxy_pass http://127.0.0.1:9003;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }

    server {
        server_name api.wowapi.org;
        listen 80;
        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
        }

        listen 443 ssl;
        ssl_certificate /keys/wowapi.org.crt;
        ssl_certificate_key /keys/wowapi.org.key;
        add_header Strict-Transport-Security "max-age=16070400; includeSubDomains; preload";

        location / {
        proxy_pass http://127.0.0.1:9004;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }


    server {
        listen 80;
        listen 443 ssl;

        server_name task.ruanjiadeng.com;

        if ($scheme = https) {
            return 301 http://$server_name$request_uri;
        }

        root   /TaskBoard/;
        index index.php index.html;


        # Make site accessible from http://localhost/
        #server_name localhost;

        location / {
            try_files $uri $uri/ /index.php?$args;
        }

        location /api {
            if (!-e $request_filename) {
                rewrite ^(.*)$ /api/api.php last; break;
            }
        }

        location /api/taskboard.db {
            rewrite ^(.*)$ /api/api.php last; break;
        }

        location ~ \.php$ {
            fastcgi_split_path_info ^(.+\.php)(/.+)$;
            # NOTE: You should have "cgi.fix_pathinfo = 0;" in php.ini

            fastcgi_pass unix:/tmp/php-cgi.sock;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_index index.php;
            include fastcgi.conf;
        }
    }

#   upstream www.google.com {
#       server 216.58.221.36:443;
#       server 216.58.221.35:443;
#       server 216.58.221.34:443;
#       server 216.58.221.33:443;
#       server 216.58.221.32:443;
#       server 216.58.221.31:443;
#   }

    server {
        listen       80  default_server;
        server_name  _;
        return       404;
    }
}
```