概念
---

> 跨站脚本（`Cross-site scripting`，通常简称为`XSS`，避免与层叠样式表css混淆）是一种网站应用程序的安全漏洞攻击，是代码注入的一种。它允许恶意用户将代码注入到网页上，其他用户在观看网页时就会受到影响。这类攻击通常包含了HTML以及用户端脚本语言。

XSS攻击通常指的是通过利用网页开发时留下的漏洞，通过巧妙的方法注入恶意指令代码到网页，使用户加载并执行攻击者恶意制造的网页程序。这些恶意网页程序通常是JavaScript，但实际上也可以包括Java，VBScript，ActiveX，Flash或者甚至是普通的HTML。攻击成功后，攻击者可能得到更高的权限（如执行一些操作）、私密网页内容、会话和cookie等各种内容。

> 跨站点请求伪造（`Cross Site Request Forgery`，简称`CORF`）。也被称为 one-click attack 或者 session riding，是一种挟制用户在当前已登录的Web应用程序上执行非本意的操作的攻击方法。跟跨网站脚本（XSS）相比，XSS 利用的是用户对指定网站的信任，CSRF 利用的是网站对用户网页浏览器的信任。

CSRF
---
先讲CORF，因为比较好理解。

跨站请求攻击，简单地说，是攻击者通过一些技术手段欺骗用户的浏览器去访问一个自己**曾经认证过的**网站并执行一些操作（如发邮件，发消息，甚至财产操作如转账和购买商品）。由于浏览器曾经认证过，所以被访问的网站会认为是真正的用户操作而去执行。这利用了web中用户身份验证的一个漏洞：**简单的身份验证只能保证请求发自某个用户的浏览器，却不能保证请求本身是用户自愿发出的。**

比如，某人登录了某个网站，这时服务器会发送cookie或session。再次访问某恶意网站时，其中含有攻击者精心伪造的资源请求网页代码（指向刚访问过的某网站），这时浏览器访问时会携带本地保存的cookie或session来进行验证，就会请求成功。

CORF并不能通过CSRF攻击来直接获取用户的账户控制权，也不能直接窃取用户的任何信息。他们能做到的，是欺骗用户浏览器，让其以用户的名义执行操作。

CORF有时和XSS互相配合使用，又称为`XSRF`。

### 浏览器的cookie策略

分为两个：

1. `Session Cookie`会话，又称为“临时Cookie”
2. `Third-party Cookie`，又称为“本地Cookie”

Third-party Cookie 是服务器在`Set-Cookie`时指定了Expire超时时间，只有到时才会失效，所以会保存在本地；

Session Cookie 则没有指定Expire时间，在浏览器关闭后失效。

如果跨域加载资源，某些浏览器因为安全原因，会阻止 Third-party Cookie 的发送。且在“P3P响应头”介入后变得复杂。

### P3P

`P3P`全称 The Platform for Privacy, 如果网站响应头里含有P3P头，则在某种程度上允许浏览器发送第三方Cookie。P3P头主要应用在类似广告等需要跨域访问的页面，但是，P3P头的影响会扩大到整个域中的所有页面，因为Cookie是以 域 和 path 为单位的。

### GET, POST?

有些网站的应用，一些重要操作并未严格区分`GET`与`POST`，攻击者可以使用GET来请求表单的提交地址。如果服务器未对请求方法进行限制，则会通过这个GET请求。

就算服务器对请求方法进行了限制，攻击者也可以构造一个form表单，使用JavaScript自动提交。

> 有个容易混淆的概念：`CORS` 跨域资源共享

>跨来源资源共享（CORS）是一份浏览器技术的规范，提供了 Web 服务从不同域传来沙盒脚本的方法，以避开浏览器的同源策略，是 JSONP 模式的现代版。与 JSONP 不同，CORS 除了 GET 要求方法以外也支持其他的 HTTP 要求。用 CORS 可以让网页设计师用一般的 XMLHttpRequest，这种方式的错误处理比 JSONP 要来的好。另一方面，JSONP 可以在不支持 CORS 的老旧浏览器上运作。现代的浏览器都支持 CORS。[更多](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS "HTTP访问控制 - MDN")

XSS
---
攻击者使被攻击者在浏览器中执行脚本后，如果需要收集来自被攻击者的数据（如cookie或其他敏感信息），可以自行架设一个网站，让被攻击者通过JavaScript等方式把收集好的数据作为参数提交，随后以数据库等形式记录在攻击者自己的服务器上。

### 常用的XSS攻击手段和目的有：

- 盗用cookie，获取敏感信息。
- 利用植入Flash，通过crossdomain权限设置进一步获取更高权限；或者利用Java等得到类似的操作。
- 利用iframe、frame、XMLHttpRequest或上述Flash等方式，以（被攻击）用户的身份执行一些管理动作，或执行一些一般的如发微博、加好友、发私信等操作。
- 利用可被攻击的域受到其他域信任的特点，以受信任来源的身份请求一些平时不允许的操作，如进行不当的投票活动。
- 在访问量极大的一些页面上的XSS可以攻击一些小型网站，实现DDoS攻击的效果。

### XSS分为：

1. 反射型（需要用户点击交互，通过）
2. 存储型（恶意脚本保存在攻击者自己的服务器上）
3. Dom Based XSS（属于反射型的一种，比较特殊）

XSS需要一个Payload来触发。

### 已经有成熟的XSS框架/平台（略）

### XSS构建技巧：

1. 字符编码
2. 长度限制
  1. location.hash
  2. window.name
3. base标签
4. 注释
5. Flash万恶之源
6. JS框架漏洞


CSRF防御
---

CSRF能成功的本质是：**重要操作的所有参数都是可以被攻击者猜到的**。

1. 验证码
2. 验证Referer请求头（不靠谱）
3. Token
  1. 一定要足够随机
  2. 目的不是防止重复提交，故短时间内可以复用
  3. 提交后重新生成

XSS防御
---

1. HttpOnly
2. 输入检查
3. 输出检查
  1. HTML Encode
  2. JS Encode
  3. CSS Encode
  4. URL Encode [URL编码](http://www.w3school.com.cn/tags/html_ref_urlencode.html)

**HTML 编码**：[常用HTML转义字符 JavaScript转义符](http://114.xixik.com/character/)

>在HTML中，定义转义字符串的原因有两个：第一个原因是像“<”和“>”这类符号已经用来表示HTML标签，因此就不能直接当作文本中的符号来使用。为了在HTML文档中使用这些符号，就需要定义它的转义字符串。当解释程序遇到这类字符串时就把它解释为真实的字符。在输入转义字符串时，要严格遵守字母大小写的规则。第二个原因是，有些字符在ASCII字符集中没有定义，因此需要使用转义字符串来表示。

转义字符串（Escape Sequence），即字符实体（Character Entity）分成三部分：

- 第一部分是一个`&`符号，英文叫ampersand；
- 第二部分是**实体（Entity）名字**或者是`#`加上**实体编号**；
- 第三部分是一个分号`;`。

**URL 编码**：网络标准[RFC 1738](http://www.ietf.org/rfc/rfc1738.txt)做了硬性规定：

>"只有字母和数字[0-9a-zA-Z]、一些特殊符号"$-_.+!*'(),"[不包括双引号]、以及某些保留字，才可以不经过编码直接用于URL。"

### 根据输出情况使用编码

1. HTML标签，HTML属性：使用HTMLEncode
2. `<script>`标签：确保输出变量在双引号里面 + JavaScriptEncode
3. 事件中：JavaScriptEncode
4. CSS中输出形成XSS多样，尽可能禁止用户可控变量在`<style>`, `style属性`以及`CSS文件`中输出。使用 OWASP ESAPI 中的`encodeForCSS()`函数。
5. 地址栏：URLEncode
6. 伪协议，如dataURI：如果不是以`http`开头则添加 + URLEncode

参考链接
----
- [跨站脚本 - 维基百科](https://zh.wikipedia.org/wiki/%E8%B7%A8%E7%B6%B2%E7%AB%99%E6%8C%87%E4%BB%A4%E7%A2%BC)
- [跨站请求伪造 - 维基百科](https://zh.wikipedia.org/wiki/%E8%B7%A8%E7%AB%99%E8%AF%B7%E6%B1%82%E4%BC%AA%E9%80%A0)
- [白帽子讲Web安全 (豆瓣)](https://book.douban.com/subject/10546925/)
- [关于URL编码 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2010/02/url_encoding.html)
- [List of Unicode characters - Wikipedia](https://en.wikipedia.org/wiki/List_of_Unicode_characters)
- <a href="https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet#RULE_.234_-_CSS_Escape_And_Strictly_Validate_Before_Inserting_Untrusted_Data_into_HTML_Style_Property_Values">CSS_Escape</a>