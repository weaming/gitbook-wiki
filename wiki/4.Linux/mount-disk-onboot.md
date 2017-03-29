关于linux开机之后自动加载挂载的分区，这块，涉及到的文件是`/etc/fstab`文件。 关于这个文件的描述说明如下: 

1. 根目录/必须载入，而且要先于其他载入点被载入 
2. 其他载入点必须为已建立的目录 
3. 若进行卸载，必须先将工作目录移到载入点及其子目录之外 

#### 查看当前分区

```shell
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            3.9G     0  3.9G   0% /dev
tmpfs           793M  9.4M  783M   2% /run
/dev/sdb1        41G  6.2G   33G  17% /
tmpfs           3.9G  106M  3.8G   3% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
/dev/sdb2        37G  2.3G   33G   7% /home
/dev/sdb4       561G  278G  283G  50% /home/garden/G
cgmfs           100K     0  100K   0% /run/cgmanager/fs
tmpfs           793M   32K  793M   1% /run/user/1000
```

#### 编辑后的`/etc/fstab`文件

```txt
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sdb1 during installation
UUID=34c097e2-8dc5-4e6c-9ad1-17b5636554d3 /               ext4    errors=remount-ro 0       1
# /home was on /dev/sdb2 during installation
UUID=b586c810-cd73-44be-ba11-e649a5dcd76d /home           ext4    defaults          0       2
/dev/sdb3 /home/garden/F ntfs nls=utf8,umask=0000 0 0
/dev/sdb4 /home/garden/G ntfs nls=utf8,umask=0000 0 0
```

1. 第一列为设备号或该设备的卷标 
1. 第二列为挂载点 
1. 第三列为文件系统 
1. 第四列为文件系统参数 
1. 第五列为是否可以用demp命令备份。0：不备份，1：备份，2：备份，但比1重要性小。设置了该参数后，Linux中使用dump命令备份系统的时候就可以备份相应设置的挂载点了。 
1. 第六列为是否在系统启动的时候，用fsck检验分区。因为有些挂载点是不需要检验的，比如：虚拟内存swap、/proc等。0：不检验，1：要检验，2要检验，但比1晚检验，一般根目录设置为1，其他设置为2就可以了。

其中最后两行是我新增的windows系统下的分区，添加进去的挂载记录。

## Links

- [linux开机自动挂载文件/etc/fstab](http://winhyt.iteye.com/blog/980749)
- [挂载Windows分区 - Ubuntu中文](http://wiki.ubuntu.org.cn/%E6%8C%82%E8%BD%BDWindows%E5%88%86%E5%8C%BA)