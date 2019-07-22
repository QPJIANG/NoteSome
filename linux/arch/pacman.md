pacman：

	pacman -S   ：安装
	
	pacman -Ss ：查询
	
	pacman -R   ：删除
	
	pacman -Rs ：删除包和其依赖
	
	pacman -Qs ：查询已安装包
	
	pacman -Qi ：显示查找的包的信息
	
	pacman -Ql：显示包的文件安装位置
	
	pacman -Sw ：下载包但不安装
	
	pacman -U  path/。。。 ： 安装本地的包
	
	pacman -Scc ： 清除缓存
	
	pacman -Syu ：升级系统的包
	
	pacman -Qm: 查找不在官方库安装的软件包
	
	pacman -Qk，pacman -Qkk: 检查安装的包是否缺少文件



	删除单个软件包，保留其全部已经安装的依赖关系
	pacman -R package_name
	
	删除指定软件包，及其所有没有被其他已安装软件包使用的依赖关系：
	pacman -Rs package_name
	
	要删除软件包和所有依赖这个软件包的程序:
	# pacman -Rsc package_name
	
	警告: 此操作是递归的，请小心检查，可能会一次删除大量的软件包。
	要删除软件包，但是不删除依赖这个软件包的其他程序：
	# pacman -Rdd package_name


	pacman 删除某些程序时会备份重要配置文件，在其后面加上*.pacsave扩展名。-n 选项可以删除这些文件：
	pacman -Rn package_name
	pacman -Rsn package_name

```
清理无用的安装包：
# pacman -Rns $(pacman -Qdtq)
$ yaourt -Qdt
```

pacman -Qlk  检查包是否损坏: sudo pacman -Qlk| grep "missing files"| grep -v "0 missing files"







```
unable to lock database

sudo rm /var/lib/pacman/db.lck
```

