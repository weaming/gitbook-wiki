滚动条通常会出现在哪些地方
--
- 浏览器边框，当页面内容超过浏览器视窗大小
- `textarea`，内容过多时
- `iframe`
- `div`或任何`block`元素，当它们的被设定成`overflow`属性时

```
overflow: scroll; /* 让它显示滚动条 */
```

如何使用
---
Webkit浏览器专属的CSS属性需要使用`-webkit-`浏览器引擎前缀

```
::-webkit-scrollbar {
      width: 15px;
} /* 这是针对缺省样式 (必须的) */
```

其他伪元素
---
```
::-webkit-scrollbar-track {
      background-color: #b46868;
} /* 滚动条的滑轨背景颜色 */

::-webkit-scrollbar-thumb {
      background-color: rgba(0, 0, 0, 0.2);
} /* 滑块颜色 */

::-webkit-scrollbar-button {
      background-color: #7c2929;
} /* 滑轨两头的箭头按钮颜色 如果省略则不显示*/

::-webkit-scrollbar-corner {
      background-color: black;
} /* 横向滚动条和纵向滚动条相交处尖角的颜色 */
```

为什么使用双冒号
---
早在CSS1里就已经有了`伪元素`的概念，但 `:before` 和 `:after` 这两个伪元素，是在CSS2.1里新出现的。

起初，伪元素的前缀使用的是单冒号语法，但随着Web的进化，在CSS3的规范里，伪元素的语法被修改成使用双冒号，成为`::before` & `::after`  这个样子，用来跟“`伪类`(pseudo-classes)”区分开，(例如 `:hover`, `:active`, 等)。

参考链接
--
- [用CSS美化你的滚动条 – WEB骇客](http://www.webhek.com/scrollbar)