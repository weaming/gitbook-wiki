## 什么是魔术方法

什么是魔术方法?他们是面向对象的Python的一切。他们是可以给你的类增加“magic”的特殊方法。他们总是被双下划线所包围(e.g. `__init__` 或者 `__lt__`)。

Python的[内置方法](https://docs.python.org/2/library/functions.html)、关键字、运算符，很多都是间接调用这些魔术方法。

参考 [Python 的 Magic Methods 指南 - 开源中国社区](http://www.oschina.net/translate/python-magicmethods)

## `__getattr__` 和 `__getattribute__` 方法的区别

`object.__getattr__(self, name)`

>Called when an attribute lookup has not found the attribute in the usual places (i.e. it is not an instance attribute nor is it found in the class tree for `self`). `name` is the attribute name. This method should return the (computed) attribute value or raise an `AttributeError` exception.

`object.__getattribute__(self, name)` The methods only apply to new-style classes.

>Called unconditionally(无条件地) to implement attribute accesses for instances of the class. If the class also defines `__getattr__`(), the latter will not be called unless `__getattribute__`() either calls it explicitly or raises an `AttributeError`. This method should return the (computed) attribute value or raise an `AttributeError` exception. In order to avoid infinite recursion in this method, its implementation should always call the base class method with the same name to access any attributes it needs, for example, `object.__getattribute__(self, name)`.

简而言之：如果在`__getattribute__`里显式调用`__getattr__`或抛出`AttributeError`异常，则会调用`__getattr__`。

## 和属性相关的魔术方法

`object.__setattr__(self, name, value)`

>Called when an attribute assignment is attempted. This is called instead of the normal mechanism (i.e. store the value in the instance dictionary). name is the attribute name, value is the value to be assigned to it.

>If `__setattr__`() wants to assign to an instance attribute, it should not simply execute `self.name = value` — this would cause a recursive call to itself. Instead, it should insert the value in the dictionary of instance attributes, e.g., `self.__dict__[name] = value`. For new-style classes, rather than accessing the instance dictionary, it should call the base class method with the same name, for example, `object.__setattr__(self, name, value)`.

这里说明了如何处理循环调用的问题。

`object.__delattr__(self, name)`

>Like `__setattr__`() but for attribute deletion instead of assignment. This should only be implemented if del obj.name is meaningful for the object.

## Pycharm 看代码利器
可以显示代码结构，`Ctrl + B`跳转到变量定义的地方。可设置背景图片（2016.02版本以后）。

下载地址： https://www.jetbrains.com/pycharm/

![](/img/1607/pycharm.png)

## 其他魔术方法
方法的作用，在源码里看到相关说明。

![](/img/1607/magicfunction.png)

## 总结

- python魔术方法用好了很方便
- python官方文档非常好，经常看看受益匪浅
- pycharm IDE：看代码利器，写代码利器

## 参考文档

- [3. Data model — Python 2.7.12 documentation](https://docs.python.org/2/reference/datamodel.html?highlight=__getattr__#object.__getattr__)