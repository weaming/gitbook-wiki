## 0.概览

- ascii：最早的，容量最小的编码方式。1个字节表示一个字符。
- unicode：加入多国字符，一般是2个字节表示一个字符，偏僻字用4个字节。缺点：浪费存储空间。
- utf-8：为了解决浪费空间的问题，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

## 维基定义

*[Unicode](https://zh.wikipedia.org/wiki/Unicode)*
> Unicode（中文：万国码、国际码、统一码、单一码）是计算机科学领域里的一项业界标准。它对世界上大部分的文字系统进行了整理、编码，使得电脑可以用更为简单的方式来呈现和处理文字。

> Developed in conjunction with the **Universal Coded Character Set** (UCS) standard and published as The Unicode Standard, the latest version of Unicode contains a repertoire of more than 128,000 characters covering 135 modern and historic scripts, as well as multiple symbol sets. 

就是说unicode是字符的**计算机二进制表示**和**真实字符**的一个对应关系（编码字符集）。

*[UTF-8](https://en.wikipedia.org/wiki/UTF-8)*

> UTF-8 is a character encoding capable of encoding all possible characters, or code points.

UTF-8是多种编码方式里最流行通用的一种。

## Stackoverflow

[View origin](http://stackoverflow.com/a/27939161/5281824)

```
A chinese character:      汉
it's unicode value:       U+6C49
convert 6C49 to binary:   01101100 01001001
```
> But wait a minute, is '01101100 01001001' one character or two characters? You knew this is one character because I told you, but when a computer reads it, it has no idea. So we need some sort of "encoding" to tell the computer to treat it as one. (The computer does not know what encoding it should use. You have to tell it when you save a character to a file and also when you read a character from a file.)

```
Binary format of bytes in sequence

1st Byte    2nd Byte    3rd Byte    4th Byte    Number of Free Bits   Maximum Expressible Unicode Value
0xxxxxxx                                                7             007F hex (127)
110xxxxx    10xxxxxx                                (5+6)=11          07FF hex (2047)
1110xxxx    10xxxxxx    10xxxxxx                  (4+6+6)=16          FFFF hex (65535)
11110xxx    10xxxxxx    10xxxxxx    10xxxxxx    (3+6+6+6)=21          10FFFF hex (1,114,111)
```

> According to the table above, if we want to store this character using the 'UTF-8' format, we need to prefix our character with some 'headers'. Our chinese character is 16 bits long (count the binary value yourself), so we will use the format on row 3 as it provides enough space:

```
Header  Place holder    Fill in our Binary   Result
1110    xxxx            0110                 11100110
10      xxxxxx          110001               10110001
10      xxxxxx          001001               10001001
```

Summary:

```
A chinese character:      汉
it's unicode value:       U+6C49
convert 6C49 to binary:   01101100 01001001
embed 6C49 as UTF-8:      11100110 10110001 10001001
```

## 1.Python的诞生比Unicode标准发布的时间还要早，所以最早的Python只支持ASCII编码
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

## 2.Python在后来添加了对Unicode的支持，以Unicode表示的字符串用`u'...'`表示
```
>>> u'中'
u'\u4e2d'
```
`\u`后面是十六进制的Unicode码。

## 如何转换
### unicode --> utf-8
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

### utf-8 --> unicode
```
>>> 'abc'.decode('utf-8')
u'abc'
>>> test = '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
>>> test
u'\u4e2d\u6587'
>>> print test
中文
```

### str --> utf-8
```
# UTF-8无法解码str
>>> a = '中'
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
>>> t = unicode(a, 'gbk')  # 会调用decode方法
>>> t
u'\u4e2d'
>>> t.encode('utf8')
'\xe4\xb8\xad'
```

上面这个现象跟终端的标准输入输出编码有关：

- CMD默认编码是GBK
- Mac Iterm2 默认编码是 UTF-8：

```
>>> import sys
>>> sys.stdin.encoding, sys.stdout.encoding
('UTF-8', 'UTF-8')
>>> sys.__stdin__.encoding, sys.__stdout__.encoding
('UTF-8', 'UTF-8')
```

### 读取txt文件
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

结果（说明了读取文件时默认是取为`str`）：

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
```
str(任意字节序列) -(decode)-> unicode -(encode with UFT-8)-> 存储、分发
```

在输入或者声明字符串的时候，尽早地使用decode方法将字符串转化成unicode编码格式；然后在程序内使用字符串的时候统一使用unicode格式进行处理，比如字符串拼接、字符串替换、获取字符串的长度等操作；最后，在输出字符串的时候（控制台/网页/文件），通过encode方法将字符串转化为你所想要的编码格式，比如utf-8等。
