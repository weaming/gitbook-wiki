>众所周知，HTTP是一个无状态协议，所以客户端每次发出请求时，下一次请求无法得知上一次请求所包含的状态数据，如何能把一个用户的状态数据关联起来呢？

>比如在淘宝的某个页面中，你进行了登陆操作。当你跳转到商品页时，服务端如何知道你是已经登陆的状态？

首先产生了 cookie 这门技术来解决这个问题，cookie 是 http 协议的一部分，它的处理分为如下几步：

1. 服务器向客户端发送 cookie。
1. 通常使用 HTTP 协议规定的 set-cookie 头操作。
1. 规范规定 cookie 的格式为 name = value 格式，且必须包含这部分。
1. 浏览器将 cookie 保存。
1. 每次请求浏览器都会将 cookie 发向服务器。

其他可选的 cookie 参数会影响将 cookie 发送给服务器端的过程，主要有以下几种：

- domain: 表示 cookie 影响的域名。子域名可读取上一级或顶级域名的cookie。
- path：表示 cookie 影响到的路径，匹配该路径才发送这个 cookie。
- expires 和 maxAge：告诉浏览器这个 cookie 什么时候过期，expires 是 UTC 格式时间，maxAge 是 cookie 多久后过期的相对时间。当不设置这两个选项时，会产生 session cookie，session cookie 是 transient 的，当用户关闭浏览器时，就被清除。一般用来保存 session 的 session_id。
- secure：当 secure 值为 true 时，cookie 在 HTTP 中是无效，在 HTTPS 中才有效。
- httpOnly：浏览器不允许脚本操作 document.cookie 去获取 cookie。一般情况下都应该设置这个为 true，这样可以避免被 xss 攻击拿到 cookie。
- SameSite：

### Cookie的 SameSite 属性

[Preventing CSRF with the same-site cookie attribute](http://www.sjoerdlangkemper.nl/2016/04/14/preventing-csrf-with-samesite-cookie-attribute/)

The `same-site` cookie attribute can be used to disable third-party usage for a specific cookie. It is set by the server when setting the cookie, and requests the browser to only send the cookie in a first-party context, i.e. when you are using the web application directly. **When another site tries to request something from the web application, the cookie is not sent.** This effectively makes `CSRF` impossible, because an attacker can not use a user’s session from his site anymore.

The server can set a same-site cookie by adding the SameSite=… attribute to the Set-Cookie header:

`Set-Cookie: key=value; HttpOnly; SameSite=strict` There are two possible values for the `same-site` attribute:

- Lax
- Strict

In the `strict` mode, the cookie is withheld with any cross-site usage. Even when the user follows a link to another website the cookie is not sent.

In `lax` mode, some cross-site usage is allowed. Specifically if the request is a `GET` request and the request is top-level. `Top-level` means that the URL in the address bar changes because of this navigation. This is not the case for `iframes, images or XMLHttpRequests`.

This table shows what cookies are sent with cross-origin requests. As you can see cookies without a `same-site` attribute (indicated by ‘normal’) are always sent. `Strict cookies` are never sent. `Lax cookies` are only send with a `top-level get request`.

![](/img/samesite.png)

## 铺垫：DNT HTTP头
From [Opt-out](https://en.wikipedia.org/wiki/Opt-out#Do_Not_Track_HTTP_header "Wikipedia, the free encyclopedia"):

>Do Not Track (`DNT`请勿跟踪) is an HTTP header field that requests that a web application or web site to disable its direct or cross-site user tracking of an individual user. The header field name is DNT and it currently accepts three values:

>
- 1, when the user does not want to be tracked (`opt out`)
- 0, when the user consents to being tracked (`opt in`)
- Null (no header sent), when the user has not expressed a preference

### P3P Header
用于跨域设置Cookie

（P3P这一块略复杂，中文资料也是极少的在抄来抄去，那我也抄一下吧:)。更具体复杂的还是要看[W3C官方标准](https://www.w3.org/TR/P3P/)）

    CP="CURa ADMa DEVa PSAo PSDo OUR BUS UNI PUR INT DEM STA PRE COM NAV OTC NOI DSP COR"

上面例子中隐私策略中 `CURa ADMa DEVa PSAo PSDo OUR BUS UNI PUR INT DEM STA PRE COM NAV OTC NOI DSP COR` 的意思是啥。 Fiddler可以方便的知道，在Fiddler 中我们可以看到如下信息：

```txt
Compact Policy token is present. A trailing 'o' means opt-out, a trailing 'i' means opt-in.

CURa
Information is used to complete the activity for which it was provided.

ADMa
Information may be used for the technical support of the Web site and its computer system.

DEVa
Information may be used to enhance, evaluate, or otherwise review the site, service, product, or market.

PSAo
Information may be used to create or build a record of a particular individual or computer that is tied to a pseudonymous identifier, without tying identified data (such as name, address, phone number, or email address) to the record. This profile will be used to determine the habits, interests, or other characteristics of individuals for purpose of research, analysis and reporting, but it will not be used to attempt to identify specific individuals.

PSDo
Information may be used to create or build a record of a particular individual or computer that is tied to a pseudonymous identifier, without tying identified data (such as name, address, phone number, or email address) to the record. This profile will be used to determine the habits, interests, or other characteristics of individuals to make a decision that directly affects that individual, but it will not be used to attempt to identify specific individuals.

OUR
We share information with ourselves and/or entities acting as our agents or entities for whom we are acting as an agent.

BUS
Info is retained under a service provider's stated business practices. Sites MUST have a retention policy that establishes a destruction time table. The retention policy MUST be included in or linked from the site's human-readable privacy policy.

UNI
Non-financial identifiers, excluding government-issued identifiers, issued for purposes of consistently identifying or recognizing the individual. These include identifiers issued by a Web site or service.

PUR
Information actively generated by the purchase of a product or service, including information about the method of payment.

INT
Data actively generated from or reflecting explicit interactions with a service provider through its site -- such as queries to a search engine, or logs of account activity.

DEM
Data about an individual's characteristics -- such as gender, age, and income.

STA
Mechanisms for maintaining a stateful session with a user or automatically recognizing users who have visited a particular site or accessed particular content previously -- such as HTTP cookies.

PRE
Data about an individual's likes and dislikes -- such as favorite color or musical tastes.

COM
Information about the computer system that the individual is using to access the network -- such as the IP number, domain name, browser type or operating system.

NAV
Data passively generated by browsing the Web site -- such as which pages are visited, and how long users stay on each page.

OTC
Other types of data not captured by the above definitions.

NOI
Web Site does not collected identified data.

DSP
The privacy policy contains DISPUTES elements.

COR
Errors or wrongful actions arising in connection with the privacy policy will be remedied by the service.
```

## 参考

- [PHP - 利用P3P实现跨域](https://sjolzy.cn/PHP-Using-P3P-to-achieve-cross-domain.html)
- [单点登录SSO的实现原理-CSDN](http://blog.csdn.net/cutesource/article/details/5838693)
- [The Platform for Privacy Preferences 1.0 (P3P1.0) Specification](https://www.w3.org/TR/P3P/)
- [node-lessons/lesson16 at master · alsotang/node-lessons](https://github.com/alsotang/node-lessons/tree/master/lesson16)