# Python 字典实现

字典通过key来索引，可以看做是关联数组，可以通过key来获取值。

## Hash表

Python字典是通过hash表来实现的。底层数据结构是一个数组。
而数组可以通过数组指针（第一个元素的地址）加上索引偏移量快速找到对应的值。

这个数组的索引(index)是通过一个`哈希函数`来获得，哈希函数的输入是字典的Key。
哈希函数的目标是使字典的所有Keys的哈希值尽量均匀地分布在数组上，而避免出现聚集的现象，否则会使查找性能下降。

Python所用的哈希函数使用的是内建的`hash`函数。而`hash()`会去调用被hash对象的`__hash__`方法。

Python对字符串的hash过程的接口和算法伪代码如下：
```text
arguments: string object
returns: hash
function string_hash:
    if hash cached:
        return it
    set len to string's length
    initialize var p pointing to 1st char of string object
    set x to value pointed by p left shifted by 7 bits
    while len >= 0:
        set var x to (1000003 * x) xor value pointed by p
        increment pointer p
    set x to x xor length of string object
    cache x as the hash so we don't need to calculate it again
    return x as the hash
```

数组起始序号为0，一个大小为`n`的数组，会使用`n-1`来对hash之后的整数值进行取余（可以通过`位与`运算来计算），
这个结果将决定对应的字典`键值对`(key-value pair)存储在数组的哪一个槽(slots)中。

然而，数组“槽”的数量是一定的，面对任意的无限量的可能Key，不可避免地会出现`碰撞`，即两个不同的key计算出的槽的位置却是一样的。
这个时候需要对“槽位”进行探测，找到还没有存储值的槽，或者Key相同的槽。

## 开放寻址
开放寻址是一种简单的碰撞解决方案。

二次探测序列(quadratic probing sequence)伪代码：
```text
j = (5*j) + 1 + perturb;
perturb >>= PERTURB_SHIFT;
use j % 2**i as the next table index;
```

## Python字典的C语言结构表示

Python对象的公共基础类：
```c
typedef struct {
    Py_ssize_t me_hash;
    PyObject *me_key;
    PyObject *me_value;
} PyDictEntry;
```

Python字典对象类：
```c
typedef struct _dictobject PyDictObject;
struct _dictobject {
    PyObject_HEAD
    Py_ssize_t ma_fill; # 已使用和已被移除的空槽总和
    Py_ssize_t ma_used; # 已使用的槽数
    Py_ssize_t ma_mask; # 槽总数-1
    PyDictEntry *ma_table; # 底层实际存储的数组
    PyDictEntry *(*ma_lookup)(PyDictObject *mp, PyObject *key, long hash);
    PyDictEntry ma_smalltable[PyDict_MINSIZE]; # 大小为8的初始数组
};
```

## 字典初始化
Python字典数组的初始大小是8
```text
returns new dictionary object
function PyDict_New:
    allocate new dictionary object
    clear dictionary's table
    set dictionary's number of used slots + dummy slots (ma_fill) to 0
    set dictionary's number of active slots (ma_used) to 0
    set dictionary's mask (ma_value) to dictionary size - 1 = 7
    set dictionary's lookup function to lookdict_string
    return allocated dictionary object
```

## 向字典添加内容
已填满的槽(上面的`ma_fill`)占数组容量超过三分之二时，会重新调整底层数组的大小。
新数组的大小是已经用的槽数量(`ma_used`)的4倍，也就是至少为原来数组大小的8/3;
但是当数组大小变得大于50000时，新数组大小将是已使用槽的2倍，也就至少原来数组大小的4/3。
同时原来的记录都会被复制到新申请的数组里。
```text
arguments: dictionary, key, value
returns: 0 if OK or -1
function PyDict_SetItem:
    if key's hash cached:
        use hash
    else:
        calculate hash
    call insertdict with dictionary object, key, hash and value
    if key/value pair added successfully and capacity over 2/3:
        call dictresize to resize dictionary's table
```

## 删除字典内容
当删除记录时（`ma_used`-1, `ma_fill`不变），不会导致重新调整大小。这会导致数组变得稀疏。

但是当添加新纪录时，`ma_used`+1，`ma_fill`可能会增加1，也可能不变（被放到了使用过的空槽里），
所以会慢慢地使数组变得稠密。

## Links

- http://www.laurentluce.com/posts/python-dictionary-implementation/
