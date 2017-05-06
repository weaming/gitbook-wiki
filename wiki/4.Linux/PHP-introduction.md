# PHP入门及服务环境配置（Nginx+PHP）

## PHP入门

PHP[维基百科](https://zh.wikipedia.org/wiki/PHP)：
>PHP（全称：PHP：Hypertext Preprocessor，即“PHP：超文本预处理器”）是一种开源的通用计算机脚本语言，尤其适用于网络开发并可嵌入HTML中使用。PHP的语法借鉴吸收C语言、Java和Perl等流行计算机语言的特点，易于一般程序员学习。PHP的主要目标是允许网络开发人员快速编写动态页面，但PHP也被用于其他很多领域。

最新版本：2015年12月3日 7.0.0发布

### 应用

PHP是一个应用范围很广的语言，特别是在网络程序开发方面。

1. 产生网页提供浏览器读取
2. 开发命令行脚本程序
3. 用户端的GUI应用程序（PHP-GTK）

使用PHP不需要任何费用，官方组织PHP Group提供了完整的程序源代码，允许用户修改、编译、扩充来使用。

### 语法

参考了Perl、C语言，而且可以集成在HTML之中。

简单的Hello World代码:

```
<?php
  echo 'Hello World!';
?>
```

PHP剖析引擎只剖析`<?php`到`?>`之间的代码，而不包含在`<?php`到`?>`之间的内容则会直接提交。

在判断语句中的HTML代码并不会被直接提交：

```
 <?php
 if (false) {
 ?>
 HTML Code
 <?php
 }
 ?>
```

**注释**

C与C++所使用的
- `/*...*/`
- `//`
和Perl的
- `#`

**数据类型**

- 四种标量类型
 - 整数型（integer）
 - 浮点数型（float）
 - 布尔型（boolean）
 - 字符串（string）
- 两种复合类型
 - 数组（array）
 - 对象（object）
- 两种特殊类型
 - NULL
 - 资源 （resource）

**变量**

- 以“$”后接变量名称来表示。
- 变量名称区分大小写。

**PHP框架**

1. Laravel
2. Symfony2
3. Thinkphp

**库**

- 内置的函数
- 很多扩展库（extension）

**源代码**

- 源代码是可以直接读取的，即使放到服务器上运行也是一样。
- 通过PHP编码器，可以保护PHP的源代码不被读取（对商业软件来说特别有需求），也可以提升运行的性能。
- 通过动态的缓存机制来提升速度。加速工具有商业版的，也有开放源代码的。

**PHP编译器**

PHP一直被当作解释器使用。

PHP编译器则将PHP从解释器中分离，为加快运行和改善与以其他编程语言编写部分的互通性。

- [PHP 语法教程](http://www.w3school.com.cn/php/)
- [PHP: PHP 手册 - Manual](https://secure.php.net/manual/zh/index.php)

## Unix系统下服务环境配置（Nginx+PHP）

网站和 web 应用程序在通常情况下，需要三样东西：

- PHP 自身
- 一个 web 服务器（Nginx、Apache、IIS）
- 一个 web 浏览器

如果需要自己配置服务器和 PHP，有两个方法将 PHP 连接到服务器上。

- 很多服务器，PHP 均有一个直接的模块接口（也叫做 SAPI）[来源](http://php.net/manual/zh/install.general.php)
- 如果 PHP 不能作为模块支持 web 服务器，总是可以将其作为 CGI 或 FastCGI 处理器来使用。

**下面将采用 FastCGI + Nginx 的方式。**

在 Unix 平台下安装 PHP 有几种方法：

- 使用配置和编译
- 使用各种预编译的包

CGI 或 FastCGI
---
FastCGI:
>快速通用网关接口（Fast Common Gateway Interface／`FastCGI`）是一种让交互程序与Web服务器通信的协议。FastCGI是早期通用网关接口（`CGI`）的增强版本。

>FastCGI致力于减少网页服务器与CGI程序之间互动的开销，从而使服务器可以同时处理更多的网页请求。

与为每个请求创建一个新的进程不同，FastCGI使用持续的进程来处理一连串的请求。这些进程由FastCGI服务器管理，而不是web服务器。 当进来一个请求时，web服务器把环境变量和这个页面请求通过一个<u>socket比如FastCGI进程与web服务器(都位于本地）</u>或者<u>一个TCP connection（FastCGI进程在远端的server farm）</u>传递给FastCGI进程。

CGI:
>通用网关接口（Common Gateway Interface/`CGI`）是一种重要的互联网技术，可以让一个客户端，从网页浏览器向执行在网络服务器上的程序请求数据。CGI描述了客户端和服务器程序之间传输数据的一种标准。

Nginx
--
![](http://i.imgur.com/fvCmqy3.png)

Nginx（发音同engine x）是一个网页服务器，它能反向代理HTTP, HTTPS, SMTP, POP3, IMAP的协议链接，以及一个负载均衡器和一个HTTP缓存。是一款面向性能设计的HTTP服务器，相较于Apache、lighttpd具有占有内存少，稳定性高等优势。

发明人是俄国人。此软件BSD-like协议下发行，可以在UNIX、GNU/Linux、BSD、Mac OS X、Solaris，以及Microsoft Windows等操作系统中运行。

整体采用**模块化设计**是nginx的一个重大特点，甚至http服务器核心功能也是一个模块。要注意的是：nginx的模块是静态的，添加和删除模块都要对nginx进行**重新编译**，这一点与Apache的动态模块完全不同。

了解Tengine：[Tengine - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/Tengine)（一个由淘宝从nginx复刻出来的HTTP服务器）

###与PHP的集成

自PHP-5.3.3起，`PHP-FPM`加入到了PHP核心，编译时加上`--enable-fpm`即可提供支持。 <u>PHP-FPM以守护进程在后台运行，Nginx响应请求后，自行处理静态请求，PHP请求则经过`fastcgi_pass`交由`PHP-FPM`处理，处理完毕后返回。</u> Nginx和PHP-FPM的组合，是一种稳定、高效的PHP运行方式


###直接安装（从安装源）

命令及提示摘要：

```
$ sudo apt-get install nginx
下列【新】软件包将被安装：
  nginx nginx-common nginx-full

21:31 root@debian:/home/weaming $ whereis nginx
nginx: /usr/sbin/nginx /etc/nginx /usr/share/nginx /usr/share/man/man1/nginx.1.gz

21:31 root@debian:/home/weaming $ nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

23:24 root@debian:/ $ nginx -V
nginx version: nginx/1.6.2
TLS SNI support enabled
configure arguments: --with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2' --with-ld-opt=-Wl,-z,relro --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-debug --with-pcre-jit --with-ipv6 --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_addition_module --with-http_dav_module --with-http_geoip_module --with-http_gzip_static_module --with-http_image_filter_module --with-http_spdy_module --with-http_sub_module --with-http_xslt_module --with-mail --with-mail_ssl_module --add-module=/tmp/buildd/nginx-1.6.2/debian/modules/nginx-auth-pam --add-module=/tmp/buildd/nginx-1.6.2/debian/modules/nginx-dav-ext-module --add-module=/tmp/buildd/nginx-1.6.2/debian/modules/nginx-echo --add-module=/tmp/buildd/nginx-1.6.2/debian/modules/nginx-upstream-fair --add-module=/tmp/buildd/nginx-1.6.2/debian/modules/ngx_http_substitutions_filter_module

```

小结：

- 默认安装了 `nginx nginx-common nginx-full` 三个包
- `whereis nginx` 查看nginx可执行程序位置
- 默认配置文件位置：`/etc/nginx/nginx.conf`。
 - 配置参考[nginx默认配置](https://gist.github.com/weaming/87c5e04f7474248bd4ae)
- `nginx -t`检查配置是否有错误
- `nginx -V`查看安装了哪些模块
- `/etc/nginx/`文件夹下还有(tree /etc/nginx/ -L 2)：

```
/etc/nginx/
├── conf.d
├── fastcgi.conf
├── fastcgi_params
├── koi-utf
├── koi-win
├── mime.types
├── nginx.conf
├── proxy_params
├── scgi_params
├── sites-available
│   └── default
├── sites-enabled
│   └── default -> /etc/nginx/sites-available/default
├── snippets
│   ├── fastcgi-php.conf
│   └── snakeoil.conf
├── uwsgi_params
└── win-utf

4 directories, 14 files
```

## PHP、php-fpm

### 直接（从安装源）安装

- [php为什么有那么多依赖程序？ - SegmentFault](https://segmentfault.com/q/1010000002547169)
- [PHP: Debian GNU/Linux 安装说明](http://php.net/manual/zh/install.unix.debian.php)

php自身分为三个东西，`php-cgi`，`php-cli`和`php-fpm`，cli则是在shell执行php的工具。

经典的功能模块有php-mysql，php-curl等等。mysql，mysqli，pdo，curl，gd，pear，xmlrpc，imagemagick字样的都是经典的包，前缀根据环境不同，可能是`php-`，可能是`php5-`

pdo用于取代mysql和mysqli连接数据库，curl用于post，gd用于生成验证码，pear和pecl用于安装扩展，xmlrpc用于通信，imagemagic用于图片处理。具体的功能，`apt-cache search php` 或者`yum search php`就能出现一句话的功能简介。

```
$ sudo apt-get install php5 php5-fpm php-apc php5-curl php5-cli php-pear php5-gd -y
```

**数据库**

```
$ sudo apt-get php-mysql php5-pgsql php5-sqlite -y
```

APT 会自动把适当的行添加到不同的 php.ini 相关文件中去，例如:

```
/etc/php5
├── cli
│   ├── conf.d
│   └── php.ini
├── fpm
│   ├── conf.d
│   ├── php-fpm.conf
│   ├── php.ini
│   └── pool.d
└── mods-available
    ├── apcu.ini
    ├── curl.ini
    ├── gd.ini
    ├── json.ini
    ├── opcache.ini
    ├── pdo.ini
    └── readline.ini
```
- [默认php.ini](https://gist.github.com/weaming/87960713d26f88c543be)
- [默认php-fpm.conf](https://gist.github.com/weaming/23ca6e95ba5b82a3fab2)
- [PHP: Unix 系统下的安装PHP](https://secure.php.net/manual/zh/install.unix.nginx.php)

**重启php-fpm:**

- [php 5.4中php-fpm 的重启、终止操作命令](http://www.cnblogs.com/zdz8207/p/3765579.html)

```
php5-fpm reload
php5-fpm restart
```
均报错。像下面这样做即可：

```
23:06 root@debian:/etc/php5 $ cat fpm/php-fpm.conf | grep pid
pid = /run/php5-fpm.pid
23:07 root@debian:/etc/php5 $ kill -USR2 `cat /run/php5-fpm.pid`
```

### php-cgi

php-cgi是 PHP 的`解释器` ，它只是个 CGI 程序，只能解析请求，返回结果，**不会进程管理**。所以就出现了一些能够调度 php-cgi 进程的程序。

### PHP-FPM

>FPM（FastCGI 进程管理器）用于替换 PHP FastCGI 的大部分附加功能，对于高负载网站是非常有用的。

修改了php.ini配置文件后，没办法平滑重启。php-fpm对此的处理机制是新的worker用新的配置，已经存在的worker处理完手上的活就可以歇着了，通过这种机制来平滑过度。

>"PHP解析器（php-cgi）会解析php.ini文件，初始化执行环境"，就是这里了。标准的CGI对每个请求都会执行这些步骤（不闲累啊！启动进程很累的说！），所以处理每个时间的时间会比较长。这明显不合理嘛！那么Fastcgi是怎么做的呢？首先，Fastcgi会先启一个master，解析配置文件，初始化执行环境，然后再启动多个worker。当请求过来时，master会传递给一个worker，然后立即可以接受下一个请求。这样就避免了重复的劳动，效率自然是高。而且当worker不够用时，master可以根据配置预先启动几个worker等着；当然空闲worker太多时，也会停掉一些，这样就提高了性能，也节约了资源。这就是fastcgi的对进程的管理。 来源：[搞不清FastCgi与PHP-fpm之间是个什么样的关系 - SegmentFault](https://segmentfault.com/q/1010000000256516)

搞笑版：
>你(PHP)去和爱斯基摩人(web服务器，如 Apache、Nginx)谈生意

>你说中文(PHP代码)，他说爱斯基摩语(C代码)，互相听不懂，怎么办？那就都把各自说的话转换成英语(FastCGI 协议)吧。

>怎么转换呢？你就要使用一个翻译机(PHP-FPM)(当然对方也有一个翻译机，那个是他自带的)
>
>我们这个翻译机是最新型的，老式的那个（PHP-CGI）被淘汰了。不过它(PHP-FPM)只有年轻人（Linux系统）会用，老头子们（Windows系统）不会摆弄它，只好继续用老式的那个。

## 后期碰到的问题
[nginx上，http状态200响应，PHP空白返回](http://www.cnxct.com/php-return-empty-result-on-nginx-without-script_filename/)

```
fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
```

# Links

- [Setting up PHP-FastCGI and nginx? Don’t trust the tutorials: check your configuration!](https://nealpoole.com/blog/2011/04/setting-up-php-fastcgi-and-nginx-dont-trust-the-tutorials-check-your-configuration/)