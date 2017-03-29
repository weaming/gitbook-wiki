ascii --> unicode --> utf-8

- ascii：最早的，容量最小的编码方式。1个字节表示一个字符。
- unicode：加入多国字符，一般是2个字节表示一个字符，偏僻字用4个字节。缺点：浪费存储空间。
- utf-8：为了解决浪费空间的问题，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

**在计算机内存中，统一使用Unicode编码。当需要保存到硬盘或者需要传输的时候，可以转换为UTF-8编码。**

1.Python的诞生比Unicode标准发布的时间还要早，所以最早的Python只支持ASCII编码
--
查看默认编码
```
>>> import sys
>>> sys.getdefaultencoding()
'ascii'
```

Python内建的ord()和chr()函数，可以把字母和对应的数字相互转换：
```
>>> ord('A')
65
>>> chr(65)
'A'
```

2.Python在后来添加了对Unicode的支持，以Unicode表示的字符串用`u'...'`表示
--
```
>>> u'中'
u'\u4e2d'
```
`\u`后面是十六进制的Unicode码。

3.unicode --> utf-8
----
```
>>> u'ABC'.encode('utf-8')
'ABC'
>>> u'中文'.encode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'
```
英文字符转换后表示的UTF-8的值和Unicode值相等（但占用的存储空间变小，2个字节变为1个字节），而中文字符转换后1个Unicode字符转化为UTF-8字符后，两个字节变为3个字节。用len()函数显示，从1个**字符长度**变为3个字符。
```
>>> len(u'中')
1
>>> len(u'中'.encode('utf-8'))
3
```

4.utf-8 --> unicode
----
```
>>> 'abc'.decode('utf-8')
u'abc'
>>> test = '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
u'\u4e2d\u6587'
>>> print test
中文
```

5.str --> utf-8
--
```
# UTF-8无法解码str
>>> a.decode('utf8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python2710\lib\encodings\utf_8.py", line 16, in decode
    return codecs.utf_8_decode(input, errors, True)
UnicodeDecodeError: 'utf8' codec can't decode byte 0xd6 in position 0: invalid continuation byte

# 而用GBK可以解码str
>>> t = a.decode('gbk')
>>> t
u'\u4e2d'
>>> t.encode('utf8')
'\xe4\xb8\xad'
```
或
```
>>> t = unicode(a, 'gbk')  # 估计调用了decode方法
>>> t
u'\u4e2d'
>>> t.encode('utf8')
'\xe4\xb8\xad'
```

读取txt文件
--
```
# coding: utf-8

import os

here = os.path.dirname(__file__)
fpath = os.path.join(here, '1.txt')
with open(fpath,'r') as f:
    print type(f)
    ls = f.xreadlines()
    print ls
    for l in ls:
        print l
        print type(l)
```

结果（说明了读取文件时默认是str）：
```
<type 'file'>
<open file 'C:\\Users\\weaming\\Desktop\\1.txt', mode 'r' at 0x05574078>
abc

<type 'str'>
中国
<type 'str'>
```

写入文件
----
```
with open(os.path.join(here, '2.txt'), 'w') as f:
    f.write(u'abc\n中文'.encode('utf8'))
```
可正确写入，显示为正常的“中文”。

如何保存 .py 源代码文件
----
- 保存：Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
- 读取：当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头（第一行或第二行）写上这一行行`# -*- coding: utf-8 -*-`

终极原则：decode early, unicode everywhere, encode finally
----
other-->unicode-->UTF8

在输入或者声明字符串的时候，尽早地使用decode方法将字符串转化成unicode编码格式；然后在程序内使用字符串的时候统一使用unicode格式进行处理，比如字符串拼接、字符串替换、获取字符串的长度等操作；最后，在输出字符串的时候（控制台/网页/文件），通过encode方法将字符串转化为你所想要的编码格式，比如utf-8等。
