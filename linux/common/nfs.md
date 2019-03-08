## 1. 安装 nfs server

```
yum install -y nfs-utils  rpcbind

rpcbind.service
nfs.service

```



## 2. 配置 nfs server

```
1. vim /etc/exports: config export path

	path *(rw,sync,no_root_squash)
	path client_ip(rw,sync,no_root_squash)

2. # exportfs
3. restart nfs service
```



## nfs client mount

	http://www.runoob.com/linux/linux-comm-mount.html
	https://www.linuxidc.com/Linux/2016-08/134666.htm
	https://blog.csdn.net/linuxnews/article/details/51350408
	
	mount:
	
	# mount nfs_server:path mount_point_path
	# mount -o loop file.iso mount_point_path
	
	# umount mount_point_path

​	
​	
	Usage: mount -V                 : print version
	       mount -h                 : print this help
	       mount                    : list mounted filesystems
	       mount -l                 : idem, including volume labels
	So far the informational part. Next the mounting.
	The command is `mount [-t fstype] something somewhere'.
	Details found in /etc/fstab may be omitted.
	       mount -a [-t|-O] ...     : mount all stuff from /etc/fstab
	       mount device             : mount device at the known place
	       mount directory          : mount known device here
	       mount -t type dev dir    : ordinary mount command
	Note that one does not really mount a device, one mounts
	a filesystem (of the given type) found on the device.
	One can also mount an already visible directory tree elsewhere:
	       mount --bind olddir newdir
	or move a subtree:
	       mount --move olddir newdir
	One can change the type of mount containing the directory dir:
	       mount --make-shared dir
	       mount --make-slave dir
	       mount --make-private dir
	       mount --make-unbindable dir
	One can change the type of all the mounts in a mount subtree
	containing the directory dir:
	       mount --make-rshared dir
	       mount --make-rslave dir
	       mount --make-rprivate dir
	       mount --make-runbindable dir
	A device can be given by name, say /dev/hda1 or /dev/cdrom,
	or by label, using  -L label  or by uuid, using  -U uuid .
	Other options: [-nfFrsvw][-o options] [-p passwdfd].



## umount

	umount /mountpoint
	
	device is busy:
	fuser