两条语句分别在两个 function 中：

    container = (yield v)
    result = generator.send(value)

>Resumes the execution and “sends” a value into the `generator function`. The `value` argument becomes the result of the **current yield expression**. The `send()` method returns the **next value yielded by the generator**, or raises `StopIteration` if the generator exits without yielding another value. When `send()` is called to start the generator, it must be called with `None` as the argument, because there is no `yield expression` that could receive the value.

- send(): `value --> container`
- yield: `v --> result` （v可以代表任意表达式）

### Demo

```
# -*- coding: utf-8 -*-
import time
def consumer():
    r = 'xxx'
    print 'r:', r
    while True:
        n = yield r+' foo'
        print 'n:', n
        print('[C] %s...' % n)
        r = 'finish.'
        #time.sleep(1)

def produce(c):
    print 'c:', c
    rv = c.send(None)
    print 'rv:', rv
    n = 0
    while n < 5:
        n = n + 1
        print('[P] Producing %s...' % n)
        r = c.send(n)
        print('[P] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
```

输出

```
c: <generator object consumer at 0x026D0940>
r: xxx
rv: xxx foo
[P] Producing 1...
n: 1
[C] 1...
[P] Consumer return: finish. foo
[P] Producing 2...
n: 2
[C] 2...
[P] Consumer return: finish. foo
[P] Producing 3...
n: 3
[C] 3...
[P] Consumer return: finish. foo
[P] Producing 4...
n: 4
[C] 4...
[P] Consumer return: finish. foo
[P] Producing 5...
n: 5
[C] 5...
[P] Consumer return: finish. foo
```