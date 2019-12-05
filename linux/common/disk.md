分区：
fdisk 
cfdisk


格式化
mkfs.bfs       mkfs.ext2      mkfs.fat       mkfs.msdos     mkfs.reiserfs  
mkfs.btrfs     mkfs.ext3      mkfs.jfs       mkfs.nilfs2    mkfs.vfat      
mkfs.cramfs    mkfs.ext4      mkfs.minix     mkfs.ntfs      mkfs.xfs 



disk uuid

`blkid /dev/sda1`





####  fdisk扩大分区容量

参考：<https://blog.csdn.net/chengxuyuanyonghu/article/details/51746234>

1、卸载磁盘

2、磁盘分区

```
fdisk /dev/sdb

p #查看磁柱号 ，记住，后面要用到
d #删除之前的分区
n #建立新分区
p #主分区
1 #第一个主分区
删除之前的分区，然后建立新分区，注意开始的磁柱号要和原来的一致（保证数据不丢失的关键步骤），结束的磁柱号默认回车使用全部磁盘。

wq #保存分区信息并退出
```

3、调整分区

```
e2fsck -f /dev/sdb1 #检查分区信息
resize2fs /dev/sdb1 #调整分区大小
```

4、重新挂载分区





查看硬盘类型：

```
cat /sys/block/*/queue/rotational的返回值
----------------------------------------------------------------------
# lsblk -d -o name,rota
NAME ROTA
sda     1
sdb     0

rota
	1: 机械盘
	0：固态盘

----------------------------------------------------------------------
sudo pacman -S smartmontools

sudo smartctl  --all  /dev/sd<a/b/c> |less
Rotation Rate:   ... rpm  :机械盘
Rotation Rate:    Solid State Device   ：固态盘

```

