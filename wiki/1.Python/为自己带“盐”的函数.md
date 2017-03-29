## 一切都是对象

在一些（还是所有？）动态语言里，所有的东西都是对象，比如 Python 和 JavaScript。刚刚想到一个此属性的用法，让函数为自己带“盐”。

## 例子

```Python
#!/usr/bin/python
# coding: utf-8

def f():
    if not hasattr(f, 'x'):
        f.x =[]
    f.x.append(3)
    return len(f.x)

assert f() == 1
assert f() == 2
assert f() == 3
```

上面函数在第一次运行时，会给自身添加一个名称为`x`的属性，并向这个 list 类型添加一个元素，最后返回 list 容器的元素个数；在后面的运行中，每运行一次，就会往容器新增一个元素。最终的效果就是，每次运行都会有不同的效果。

一般的想法是为此编写一个`类`，把这个属性作为类属性或者实例属性。上面这样写的话，就免去了类的那种的写法。想一想，这种写法，还是受到了 JavaScript 的启发 :-)

（更甚者，还可以实现像 JavaScript 的那种 prototype 的继承链机制。）
