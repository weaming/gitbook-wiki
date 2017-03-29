特殊变量
--
```
$# 传给脚本的参数个数
$0 脚本本身的名字
$1 传递给该shell脚本的第1个参数
$2 传递给该shell脚本的第2个参数
$@ 传给脚本的所有参数的列表
$* 以一个单字符串显示所有向脚本传递的参数，与位置变量不同，参数可超过9个
$$ 脚本运行的当前进程ID号
$? 命令执行结果反馈，0表示执行成功，其余数字表示执行不成功。
```

**测试：**

保存为`test.sh`

```
#!/bin/sh
echo "\$#:$#"
echo "\$0:$0"
echo "\$1:$1"
echo "\$2:$2"
echo "\$@:$@"
echo "\$*:$*"
echo "\$$:$$"
echo "\$?:$?"
```

执行

```
./test.sh x y
```


流、重定向、管道(pipeline)
---
**文件描述符(File Descriptor)**，用一个数字（通常为0-9）来表示一个文件。

常用输入输出操作符是：

```
1.  标准输入    (stdin) ：代码为 0 ，使用 < 或 << ； 代表：/dev/stdin
2.  标准输出    (stdout)：代码为 1 ，使用 > 或 >> ； 代表：/dev/stdout
3.  标准错误输出(stderr)：代码为 2 ，使用 2> 或 2>> ； 代表：/dev/stderr
```
其中stdout可写作`-`

**重定向（到/从文件）**

- 覆盖：`>`、`<`
- 追加：`>>`

**管道（pipeline）**

>一个由标准输入输出链接起来的进程集合，所以每一个进程的输出（stdout）被直接作为下一个进程的输入（stdin）。 每一个链接都由未命名管道实现。

注意：管道仅将 `stdout` 导向 `stdin`

test命令
----
作用：

- 检查文件类型
- 比较值

```
man test
```

```
NAME
       test - check file types and compare values
SYNOPSIS
       test EXPRESSION
       test

       [ EXPRESSION ]
       [ ]
       [ OPTION

DESCRIPTION
       Exit with the status determined by EXPRESSION.
```

test 命令最短的定义可能是评估一个表达式；如果条件为真，则返回一个 0 值。如果表达式不为真，则返回一个大于 0 的值 — 也可以将其称为假值（Uinux成功运行的退出码为0）。

**检查最后所执行命令的状态的最简便方法是使用 `$?` 值。**

**test 和 [ 命令**

　　虽然 Linux 和 UNIX 的每个版本中都包含 `test` 命令，但该命令有一个更常用的`别名(alias命令)` —— 左方括号：`[`。test 及其别名通常都可以在 /usr/bin 或 /bin （取决于操作系统版本和供应商）中找到。

　　当您使用左方括号而非 test 时，其后必须始终跟着`一个空格、要评估的条件、一个空格和右方括号`。右方括号不是任何东西的别名，而是表示所需评估参数的结束。条件两边的空格是必需的，这表示要调用 test，以区别于同样经常使用方括号的字符/模式匹配操作。

**test 文件运算符**

利用这些运算符，您可以在程序中根据对文件类型的评估结果执行不同的操作：

```shell
-b file 如果文件为一个块特殊文件，则为真
-c file 如果文件为一个字符特殊文件，则为真
-d file 如果文件为一个目录，则为真
-e file 如果文件存在，则为真
-f file 如果文件为一个普通文件，则为真
-g file 如果设置了文件的 SGID 位，则为真
-G file 如果文件存在且归该组所有，则为真
-k file 如果设置了文件的粘着位，则为真
-O file 如果文件存在并且归该用户所有，则为真
-p file 如果文件为一个命名管道，则为真
-r file 如果文件可读，则为真
-s file 如果文件的长度不为零，则为真
-S file 如果文件为一个套接字特殊文件，则为真
-t fd 如果 fd 是一个与终端相连的打开的文件描述符（fd 默认为 1），则为真
-u file 如果设置了文件的 SUID 位，则为真
-w file 如果文件可写，则为真
-x file 如果文件可执行，则为真
```


shell里的小括号,大括号结构和有括号的变量的区别
---
```js
1.${var}    # 普通变量
2.$(cmd)    # 命令替换，相当于`command`; shell会将其中的命令执行一遍，用其输出替换
3.()和{}
4.${var:-string},${var:+string},${var:=string},${var:?string} # 几种特殊的替换结构
5.$((expr))    # POSIX标准的扩展计算（man expr 查看帮助）
# 注意：这种扩展计算是整数型的计算，不支持浮点型.若是逻辑判断，表达式exp为真则为1,假则为0。
6.$(var%pattern),$(var%%pattern),$(var#pattern),$(var##pattern) # 四种模式匹配替换结构
```

`()`和`{}`都是对一串的命令进行执行，但有所区别：

```
A,()只是对一串命令重新开一个子shell进行执行
B,{}对一串命令在当前shell执行

C,()和{}都是把一串的命令放在括号里面，并且命令之间用;号隔开
D,()最后一个命令可以不用分号
E,{}最后一个命令要用分号
F,()里的各命令不必和括号有空格
G,{}的第一个命令和左括号之间必须要有一个空格

H,()和{}中括号里面的某个命令的重定向只影响该命令，但括号外的重定向则影响到括号里的所有命令
```

其他请参考[这里](http://my.oschina.net/xiangxw/blog/11407)。




设备文件
----
设备管理是 Linux 中比较基础的知识，与内核的关系也比较密切。

Linux 中的设备按照存取方式的不同，可以分为两种：

- 字符设备：无缓冲且只能顺序存取
- 块设备：有缓冲且可以随机(乱序)存取

而按照是否对应物理实体，也可以分为两种：

- 物理设备：对实际存在的物理硬件的抽象
- 虚拟设备：不依赖于特定的物理硬件，仅是内核自身提供的某种功能

无论是哪种设备，在 `/dev` 目录下都有一个对应的文件(节点)，并且每个设备文件都必须有主/次设备号，主设备号相同的设备是同类设备，使用同一个驱动程序(虽然目前的内核允许多个驱动共享一个主设备号，但绝大多数设备依然遵循一个驱动对应一个主设备号的原则)。可以通过 `cat /proc/devices `命令查看当前已经加载的设备驱动程序的主设备号。

抄录如下： [@](http://www.jinbuguo.com/kernel/device_files.html)

```
下面列出了 Linux-3.13.2 内核中常见的已注册设备及其含义(省略了生僻与罕见的设备)。
----------------------------------------------------------------------
主设备号     设备类型
          次设备号=文件名      简要说明
----------------------------------------------------------------------

  0         未命名设备(例如NFS之类非设备的挂载)
          0 = 为空设备号保留

          参见主设备号为144,145,146的块设备，以了解"扩展区域"(expansion area)


  1 char    内存设备
          1 = /dev/mem         物理内存的全镜像。可以用来直接存取物理内存。
          2 = /dev/kmem        内核看到的虚拟内存的全镜像。可以用来访问内核中的内容(查看内核变量或用作rootkit之类)。
          3 = /dev/null        空设备。任何写入都将被直接丢弃(但返回"成功")；任何读取都将得到EOF(文件结束标志)。
          4 = /dev/port        存取I/O端口
          5 = /dev/zero        零流源。任何写入都将被直接丢弃(但返回"成功")；任何读取都将得到无限多的二进制零流。
          7 = /dev/full        满设备。任何写入都将失败，并把errno设为ENOSPC(没有剩余空间)；任何读取都将得到无限多的二进制零流。
                               这个设备通常被用来测试程序在遇到磁盘无剩余空间错误时的行为。
          8 = /dev/random      真随机数发生器。以背景噪声数据或硬件随机数发生器作为熵池，读取时会返回小于熵池噪声总数的随机字节。
                               若熵池空了，读操作将会被阻塞，直到收集到了足够的环境噪声为止。建议用于需要生成高强度密钥的场合。
                               [注意]虽然允许写入，但企图通过写入此文件来"预存"随机数是徒劳的，因为写入的数据对输出并无影响。
          9 = /dev/urandom     伪随机数发生器。更快，但是不够安全。仅用于对安全性要求不高的场合。
                               即使熵池空了，读操作也不会被阻塞，而是把已经产生的随机数做为种子来产生新的随机数。
                               [注意]虽然允许写入，但企图通过写入此文件来"预存"随机数是徒劳的，因为写入的数据对输出并无影响。
         10 = /dev/aio         异步I/O通知接口
         11 = /dev/kmsg        任何对该文件的写入都将作为printk的输出；而读取则得到printk的输出缓冲区内容。

 10 char    各种杂项设备(含非串口鼠标)
          1 = /dev/psaux       PS/2鼠标
        128 = /dev/beep        能够让主板的蜂鸣器发出不同频率声音的设备(Fancy Beeper Daemon)
        130 = /dev/watchdog    看门狗(CONFIG_WATCHDOG)
        131 = /dev/temperature 机器内部温度
        135 = /dev/rtc         实时时钟(Real Time Clock)
        143 = /dev/pciconf     PCI配置空间
        144 = /dev/nvram       非易失配置RAM
        151 = /dev/led         发光二极管(LED)灯
        152 = /dev/kpoll       内核轮询(Poll)驱动
        156 = /dev/lcd         液晶(LCD)显示屏
        161 = /dev/userdma     用户空间DMA访问
        162 = /dev/smbus       系统管理总线(System Management Bus)
        164 = /dev/ipmo        Intel的智能平台管理(Intelligent Platform Management)接口
        165 = /dev/vmmon       VMware虚拟机监视器
        170 = /dev/thinkpad/thinkpad    Thinkpad设备
        173 = /dev/ipmikcs     智能平台管理(Intelligent Platform Management)接口
        175 = /dev/agpgart     AGP图形地址重映射表(Graphics Address Remapping Table)
        182 = /dev/perfctr     性能监视计数器
        183 = /dev/hwrng       通用硬件随机数发生器
        184 = /dev/cpu/microcode        CPU微代码更新接口(依赖于CONFIG_MICROCODE)
        186 = /dev/atomicps    进程状态数据的原子快照
        188 = /dev/smbusbios   SMBus(系统管理总线) BIOS
        189 = /dev/ussp_ctl    用户空间串口控制器
        200 = /dev/net/tun     TAP/TUN 网络设备(TAP/TUN以软件的方式实现了网络设备)
                               TAP模拟了以太网帧(第二层)，TUN模拟了IP包(第三层)。
        202 = /dev/emd/ctl     增强型 Metadisk RAID (EMD) 控制器
        203 = /dev/cuse        用户空间的字符设备(Character device in user-space)
        212 = /dev/watchdogs/0 第一只看门狗
        213 = /dev/watchdogs/1 第二只看门狗
        214 = /dev/watchdogs/2 第三只看门狗
        215 = /dev/watchdogs/3 第四只看门狗
        220 = /dev/mptctl      Message passing technology (MPT) control
        223 = /dev/input/uinput         用户层输入设备
        224 = /dev/tpm         TCPA TPM driver
        227 = /dev/mcelog      X86_64 Machine Check Exception driver
        228 = /dev/hpet        高精度事件定时器(HPET)
        229 = /dev/fuse        Fuse(用户空间的虚拟文件系统)
        231 = /dev/snapshot    系统内存快照
        232 = /dev/kvm         内核虚构机(基于AMD SVM和Intel VT硬件虚拟技术)
        234 = /dev/btrfs-control        Btrfs文件系统控制设备
        235 = /dev/autofs      Autofs控制设备
        236 = /dev/mapper/control       设备映射(Device-Mapper)控制器
        237 = /dev/loop-control         回环设备控制器
        238 = /dev/vhost-net   用于 virtio net 的宿主内核加速器

 11 block   SCSI CD-ROM 设备
          0 = /dev/scd0        第1个 SCSI CD-ROM
          1 = /dev/scd1        第2个 SCSI CD-ROM
            ...

 13 char    核心输入设备
          0 = /dev/input/js0   第一个游戏杆(joystick)
          1 = /dev/input/js1   第二个游戏杆(joystick)
            ...
         32 = /dev/input/mouse0         第1个鼠标
         33 = /dev/input/mouse1         第2个鼠标
            ...
         63 = /dev/input/mice  所有鼠标的合体
         64 = /dev/input/event0         第1个事件队列
         65 = /dev/input/event1         第2个事件队列
            ...

 29 char    通用帧缓冲(frame buffer)设备
          0 = /dev/fb0         第1个帧缓冲设备
          1 = /dev/fb1         第2个帧缓冲设备
            ...
         31 = /dev/fb31        第32个帧缓冲设备

 43 block   网络块设备(Network block devices)
          0 = /dev/nb0         第1个网络块设备
          1 = /dev/nb1         第2个网络块设备
            ...

119 char    VMware虚拟网路控制器
          0 = /dev/vnet0       第1个虚拟网路
          1 = /dev/vnet1       第2个虚拟网路
            ...

180 char    USB字符设备
          0 = /dev/usb/lp0      第1个USB打印机
            ...
         15 = /dev/usb/lp15     第16个USB打印机
         48 = /dev/usb/scanner0 第1个USB扫描仪
            ...
         63 = /dev/usb/scanner15  第16个USB扫描仪
         96 = /dev/usb/hiddev0  第1个USB人机界面设备(鼠标/键盘/游戏杆/手写版等)
            ...
        111 = /dev/usb/hiddev15 第16个USB人机界面设备(鼠标/键盘/游戏杆/手写版等)
        132 = /dev/usb/idmouse  ID Mouse (指纹扫描仪)

180 block   USB块设备
          0 = /dev/uba         第1个USB块设备
          8 = /dev/ubb         第2个USB块设备
         16 = /dev/ubc         第3个USB块设备
             ...

192 char    内核 profiling 接口
          0 = /dev/profile     Profiling 控制设备
          1 = /dev/profile0    CPU 0 的 Profiling 设备
          2 = /dev/profile1    CPU 1 的 Profiling 设备
            ...

193 char    内核事件跟踪接口
          0 = /dev/trace       跟踪控制设备
          1 = /dev/trace0      CPU 0 的跟踪设备
          2 = /dev/trace1      CPU 1 的跟踪设备
            ...

195 char    Nvidia 图形设备(比如显卡)
          0 = /dev/nvidia0     第1个 Nvidia 卡
          1 = /dev/nvidia1     第2个 Nvidia 卡
            ...
        255 = /dev/nvidiactl   Nvidia卡控制设备

202 char    特定于CPU模式的寄存器(model-specific register,MSR)
          0 = /dev/cpu/0/msr   CPU 0 的 MSRs
          1 = /dev/cpu/1/msr   CPU 1 的 MSRs
            ...

202 block   Xen 虚拟块设备
          0 = /dev/xvda        第1个 Xen 虚拟磁盘(整块磁盘)
         16 = /dev/xvdb        第2个 Xen 虚拟磁盘(整块磁盘)
         32 = /dev/xvdc        第3个 Xen 虚拟磁盘(整块磁盘)
            ...
        240 = /dev/xvdp        第16个 Xen 虚拟磁盘(整块磁盘)

          [说明]分区的表示方法与SCSI磁盘相同(最大15个)

203 char    CPU CPUID 信息
          0 = /dev/cpu/0/cpuid  CPU0的CPUID
          1 = /dev/cpu/1/cpuid  CPU1的CPUID
            ...

226 char    DRI(Direct Rendering Infrastructure)
          0 = /dev/dri/card0   第1个显卡
          1 = /dev/dri/card1   第2个显卡
            ...

232 char    生物识别设备
          0 = /dev/biometric/sensor0/fingerprint  第1个设备的第1个指纹传感器
          1 = /dev/biometric/sensor0/iris         第1个设备的第1个虹膜传感器
          2 = /dev/biometric/sensor0/retina       第1个设备的第1个视网膜传感器
          3 = /dev/biometric/sensor0/voiceprint   第1个设备的第1个声波传感器
          4 = /dev/biometric/sensor0/facial       第1个设备的第1个面部传感器
          5 = /dev/biometric/sensor0/hand         第1个设备的第1个手掌传感器
            ...
         10 = /dev/biometric/sensor1/fingerprint  第2个设备的第1个指纹传感器
            ...
         20 = /dev/biometric/sensor2/fingerprint  第3个设备的第1个指纹传感器
```

更多
---
参见：[linux下常用的命令用法](/note/linux-commands/)