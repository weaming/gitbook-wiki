我在页面中添加了个人豆瓣读书的[展示](/book)

代码如下：

![](http://neilimg.b0.upaiyun.com/screenshots/douban-book.png)

然后在页面中添加如下内容，其中用到了[flexbox](/note/flexbox)弹性盒的css样式。

```
<style>
	#book>div{
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: space-around;
		align-items: baseline;
	}
	#book img {height: 400px;}
	#book div, #book a{text-align: center;}
</style>

<div id="book">
	<h2>我读过的书</h2>
	<div id="read"></div>
	<h2>我想读的书</h2>
	<div id="wish"></div>
</div>

<script type="text/javascript" src="/js/book.js"></script>
```

另外还有官方的service：[豆瓣收藏秀(JS版)](https://www.douban.com/service/badgemakerjs)。我用它来添加了[个人电影页面](/movie)