参考：

<https://blog.csdn.net/ikikik2002/article/details/5187276>

<https://www.linuxidc.com/Linux/2018-06/152992.htm>



```bash
安装lvm 工具

为了使用LVM，要确保在系统启动时激活LVM，在RedHa的版本中，系统启动脚本已具有对激活LVM的支持，在/etc/rc.d/rc.sysinit中有以下内容：
　
if [ -x /sbin/lvm.static ]; then
          action $"Setting up Logical Volume Management:" /sbin/lvm.static vgchange -a y --ignorelockingfailure
fi
vgchange -a y命令激活系统所有卷组。
------------------------------------------------------------------------------------------
/boot分区用于存放引导文件，不能应用LVM机制  (/boot/efi，/boot : centos 默认都是不使用lvm 的)
------------------------------------------------------------------------------------------

物理卷 （PV, Physical Volume） : 整个硬盘，或使用fdisk等工具建立的普通分区
	fdisk 分区类型设置为“8e”
	创建：
	pvcreate 设备名
	# pvcreate /dev/sdb
	# pvcreate /dev/sdc1
	# pvcreate /dev/sdb /dev/sdc1
	[设备名对应物理卷名: 与卷组创建命令相关]
	
	
	查看：
	# lvmdiskscan   （包含 LVM physical volume 的分区）
	# pvs ，pvscan ，pvdisplay
	
	移除：
	pvremove /dev/sdb
	
卷组（VG, Volume Group）:一个或多个物理卷组合而成的整体
	vgcreate 卷组名 物理卷名1 物理卷名2
	# vgcreate mail_store /dev/sdb /dev/sdc1
	vgremove
	
	vgexted
	
	
	

逻辑卷（LV, Logical Volume） : 从卷组中分割出的一块空间，用于建立文件系统 
	lvcreate -L 大小 -n 逻辑卷名 卷组名
	
	lvremove
	
	扩展：
	lvextend -L +大小 /dev/卷组名/逻辑卷名
	
	扩容步骤：调整逻辑卷大小→调整文件系统大小
	# lvextend -L +10G  /dev/mail_store/mail   #调整逻辑卷大小
	# e2fsck -f /dev/mail_store/mail  -y   #检查逻辑卷
	# resize2fs /dev/mail_store/mail 
	
	缩容步骤：调整文件系统大小→调整逻辑卷大小
	# lvextend -l +100%free  /dev/mail_store/mail
	# resize2fs -p /dev/mail_store/mail 10G  　　　　//-p打印进度，将mail缩小至10G
	# lvreduce -L 10G /dev/mail_store/mail 　　　　　//将逻辑卷缩小至10G
	
	格式化： 与普通硬盘分区格式化一致  ： mkfs
	挂载： mount   (开机挂载写入 /etc/fstab)
	
------------------------------------------------------------------------------------------
	/etc/fstab
	# <file system> <mount point> <type> <options> <dump> <pass>
	uuid=[blkid 获取块设备id] 文件系统类型  文件类型 <options> <dump> <pass>
	物理卷名 挂载点  文件系统类型 <options> <dump> <pass>
	
	
	
	文件系统类型：
		Linux可以使用ext2、ext3等类型，此字段须与分区格式化时使用的类型相同。
		也可以使用 auto 这一特殊的语法，使系统自动侦测目标分区的分区类型。auto通常用于可移动设备的挂载。
		
	options：
        auto: 系统自动挂载，fstab默认就是这个选项
        defaults: rw, suid, dev, exec, auto, nouser, and async.
        noauto 开机不自动挂载
        nouser 只有超级用户可以挂载
        ro 按只读权限挂载
        rw 按可读可写权限挂载
        user 任何用户都可以挂载
        请注意光驱和软驱只有在装有介质时才可以进行挂载，因此它是noauto
	
	dump备份设置：
		当其值设置为1时，将允许dump备份程序备份；设置为0时，忽略备份操作；
		
	fsck磁盘检查设置	
		其值是一个顺序。当其值为0时，永远不检查；
		而 / 根目录分区永远都为1。其它分区从2开始，数字越小越先检查
		如果两个分区的数字相同，则同时检查。
------------------------------------------------------------------------------------------
	
	
	
```

| 功能 | 物理卷管理 | 卷组管理  | 逻辑卷管理 |
| ---- | ---------- | --------- | ---------- |
| 扫描 | pvscan     | vgscan    | lvscan     |
| 创建 | pvcreate   | vgcreate  | lvcreate   |
| 显示 | pvdisplay  | vgdisplay | lvdisplay  |
| 删除 | pvremove   | vgremove  | lvremove   |
| 扩展 |            | vgextend  | lvextend   |



```
使用lvm技术可以扩大根分区，不破坏分区表。
1：首先新加一块磁盘，连接至主机。开机，进入系统。使用root登录，运行fdisk，将新加的磁盘分区。我们这里假设将全部磁盘容量只分一个区，分区 为/dev/sdb1;
2：创建pv: pvcreate /dev/sdb1
3:扩展VG：vgextend /dev/VolGroup00 /dev/sdb1
4:运行vgdisplay ，查看扩展后的VG，如果显示容量增加，表示，VG扩展成功；
5：扩展LV： lvextend -L + n(M,或G） /dev/VolGroup00/LogVol00 /dev/VolGroup00
重新启动机器，进入Resuce 模式，装载磁盘时选择skipp。

6：激活VG： 运行 lvm vgchange -a y /dev/VolGgroup00
7:调整文件系统大小： 首先运行 e2fsck 检查文件系统。 e2fsck /dev/VolGroup00/LogVol00
8:resize2fs /dev/VolGroup00/LogVol00
```

