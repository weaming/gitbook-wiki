#《淘宝全站https》点评摘要

>HTTPS = HTTP + SSL/TSL
>
>SSL 安全套接层（Secure Sockets Layer）；TLS 传输层安全协议（Transport Layer Security）。SSL是TLS的前身。

来源：[启用全站HTTPS后不仅更安全而且更快 看淘宝是如何做到的](http://weibo.com/p/1001603948661200565978)

启用HTTPS必须解决的难题：

- HTTPS需要多次握手，因此网络耗时变长，用户从HTTP跳转到HTTPS需要一些时间
- HTTPS要做RSA校验，这会影响到设备性能
- 所有CDN节点要支持HTTPS，而且需要有极其复杂的解决方案来面对DDoS的挑战
- 周边兼容性：
	- 页面里所有嵌入的资源都要改成HTTPS的，这些资源可能会来自不同的部门甚至不同的公司，包括图片、视频、表单等等，否则浏览器就会报警
	- 移动客户端（APP）也需要适配HTTPS
	- 第三方网站看不到Referer的问题
	- 开发、测试环境都要做HTTPS的升级

这里有几个概念详细说明下：

- 多次握手及RSA校验（[SSL/TLS协议运行机制的概述](http://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)）
- RSA加密算法是一种非对称加密算法（[RSA算法原理](http://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html)）

>（1）乙方生成两把密钥（公钥和私钥）。公钥是公开的，任何人都可以获得，私钥则是保密的。

>（2）甲方获取乙方的公钥，然后用它对信息加密。

>（3）乙方得到加密后的信息，用私钥解密。

- CDN 内容分发网络：比如国内的`蓝讯`和`网宿`，最近比较火的`七牛`、`又拍云`，国外的`CloudFlare`、`KeyCDN`、`Akamai`等

>内容分发网络（Content delivery network或Content distribution network，缩写：`CDN`）是指一种通过互联网互相连接的电脑网络系统，利用最靠近每位用户的服务器，更快、更可靠地将音乐、图片、视频、应用程序及其他文件发送给用户，来提供高性能、可扩展性及低成本的网络内容传递给用户。

**“而据阿里巴巴技术保障部技术专家李振宇介绍，阿里电商在启用全站HTTPS后，性能不降反升，用户访问网站和移动端更为流畅。”**

>比如以域名收敛的方式减少建连；采用`HSTS技术`去掉80到443的`302跳转`；通过Session复用来提高建连速度和降低服务器压力；对证书链进行优化以减少证书的传输量等等。

### 域名收敛：[无线性能优化：域名收敛 | Taobao FED | 淘宝前端团队](http://taobaofed.org/blog/2015/12/16/h5-performance-optimization-and-domain-convergence/)

- DNS 的解析方式：
- 迭代解析：DNS 服务器之间就是的交互查询就是迭代查询
- 递归解析：从客户端到本地 DNS 服务器（又称 Local DNS ，就是你电脑里面配置的或者 DHCP 分配的）是属于递归查询
- 所以减少开销就两条路，第一个就是减少 DNS 的请求，第二个就是缩短 DNS 解析路径。
 - 将相关域名收敛成一个
 - 第一个就是做域名收敛的主要原因，于 PC 是对于域名的并发限制，无线上来说对并发的要求会弱很多（一般尽量是第一屏，后面使用懒加载）。
 - 第二个就是缩短解析路径，这里所说的缩短解析路径其实就说各级的缓存：本机的缓存，LocalDNS 的缓存。不过他们或多或少也不靠谱，尤其是运营商的 LocalDNS 给你劫持一下，篡改一下都是常有的事情，于是这个情况下，就有了`HttpDNS`。

### HttpDNS原理：将域名解析的协议由DNS协议换成了Http协议，由HTTP API来获取解析结果

![](http://neilimg.b0.upaiyun.com/screenshots/httpdnsjbyl.png)

- 传统DNS解析：客户端发送udp数据包到dns服务器,dns服务器返回该域名的相关A记录信息。
- HTTPDNS解析：客户端发起http请求携带需要查询的域名,通过IP直接访问服务器,该Http服务器接倒请求后返回域名对应的A记录。

>淘宝：采用了双证书模式，即`SHA-1`和`SHA-256`，此举的目的在于最大限度地保证安全和兼容性。同时，阿里巴巴使用的是兼容性最宽泛的OV证书，全面支持单域名、多域名和`泛域名`，尽管费用较为昂贵，但能够满足多种浏览器访问，保证最好的用户体验。

**SHA2**

>[SHA-2](https://zh.wikipedia.org/wiki/SHA-2)，名称来自于安全散列算法2（英语：Secure Hash Algorithm 2）的缩写，一种密码杂凑函数算法标准，由美国国家安全局研发，由美国国家标准与技术研究院（NIST）在2001年发布。属于SHA算法之一，是SHA-1的后继者。其下又可再分为六个不同的算法标准，包括了 `SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256`。

优化算法

>淘宝无线基于TLS1.3协议进行了改造，在保障链路安全的情况下优化SSL握手过程实现零耗时提升了用户体验，摒弃传统的RSA算法，转而使用了最新的ECDH密钥交换算法

### 关于SSLv3不安全:[博客开始使用https · Neil](/2016/03/https/)

>目前，应用最广泛的是TLS 1.0，接下来是SSL 3.0。但是，主流浏览器都已经实现了TLS 1.2的支持。TLS 1.0通常被标示为SSL 3.1，TLS 1.1为SSL 3.2，TLS 1.2为SSL 3.3。[SSL/TLS协议运行机制的概述](http://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)

>**2014年10月，Google发布在SSL 3.0中发现设计缺陷，建议禁用此一协议。**攻击者可以向TLS发送虚假错误提示，然后将安全连接强行降级到过时且不安全的SSL 3.0，然后就可以利用其中的设计漏洞窃取敏感信息。Google在自己公司相关产品中陆续禁止向后兼容，强制使用TLS协议。Mozilla也在11月25日发布的Firefox 34中彻底禁用了SSL 3.0。微软同样发出了安全通告。[传输层安全协议TLS](https://zh.wikipedia.org/wiki/%E5%82%B3%E8%BC%B8%E5%B1%A4%E5%AE%89%E5%85%A8%E5%8D%94%E8%AD%B0)
>
SSLv1.0版本从未公开过，因为存在严重的安全漏洞。SSLv2.0版本在1995年2月发布，但因为存在数个严重的安全漏洞而被3.0版本替代。
SSLv3.0版本在1996年发布，是由网景工程师Paul Kocher、Phil Karlton和Alan Freier完全重新设计的。较新版本的SSL/TLS基于SSL 3.0。

#### 发表日期：

协议|年份|协议|年份
---|---|---|---
SSL 1.0	|N/A|TLS 1.0	|1999
SSL 2.0	|1995|TLS 1.1	|2006
SSL 3.0	|1996|TLS 1.2	|2008
TLS 1.3	|待定

（关注TLSv1.3 [The Transport Layer Security (TLS) Protocol Version 1.3](http://tlswg.github.io/tls13-spec/)）

>从技术上讲，TLS 1.0与SSL 3.0的差异非常微小。TLS 1.0可以降级到SSL 3.0，这削弱了连接的安全性

#### Nginx 中禁用SSLv3

```
ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
```