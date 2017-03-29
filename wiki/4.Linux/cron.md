## 介绍

crontab命令常见于Unix和类Unix的操作系统之中，用于设置周期性被执行的指令。该命令从标准输入设备读取指令，并将其存放于“crontab”文件中，以供之后读取和执行。该词来源于希腊语 chronos(χρόνος)，原意是时间。

通常，crontab储存的指令被守护进程激活， crond常常在后台运行，每一分钟检查是否有预定的作业需要执行。这类作业一般称为cron jobs。

## 安装

CentOS安装cron：`yum install vixie-cron -y`

## 配置

`/etc/crontab` 文件中的每一行都代表一项任务，它的格式是：

```
minute   hour   day   month   dayofweek   command

minute — 分钟，从 0 到 59 之间的任何整数
hour — 小时，从 0 到 23 之间的任何整数
day — 日期，从 1 到 31 之间的任何整数（如果指定了月份，必须是该月份的有效日期）
month — 月份，从 1 到 12 之间的任何整数（或使用月份的英文简写如 jan、feb 等等）
dayofweek — 星期，从 0 到 7 之间的任何整数，这里的 0 或 7 代表星期日（或使用星期的英文简写如 sun、mon 等等）
command — 要执行的命令（命令可以是 ls /proc >> /tmp/proc 之类的命令，也可以是执行你自行编写的脚本的命令。）
```

- 在以上任何值中，星号（`*`）可以用来代表所有有效的值。譬如，月份值中的星号意味着在满足其它制约条件后每月都执行该命令。
- 整数间的短线（`-`）指定一个整数范围。譬如，1-4 意味着整数 1、2、3、4。
- 用逗号（`,`）隔开的一系列值指定一个列表。譬如，3, 4, 6, 8 标明这四个指定的整数。
- 正斜线（`/`）可以用来指定间隔频率。在范围后加上 `/<integer>` 意味着在范围内可以跳过 integer。譬如，`0-59/2` 可以用来在分钟字段定义每两分钟。间隔频率值还可以和星号一起使用。例如，`*/3` 的值可以用在月份字段中表示每三个月运行一次任务。
- 开头为井号（`#`）的行是注释，不会被处理。

比如我的配置示例： `$ cat /etc/crontab`

```
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
HOME=/

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed

0 */3 * * * www /usr/bin/php /www/ttrss/update.php --feeds --quiet
0 3 * * * root /etc/init.d/shadowsocks restart
```