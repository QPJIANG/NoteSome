```
列举源
yum repolist [all|enabled|disabled]

清理缓存
yum clean [ packages | metadata | expire-cache | rpmdb | plugins | all ]

创建缓存
yum makecache 

查看所有仓库的可用软件包
yum list 
	yum list {available|updates|installed|extras|obsoletes} [glob_exp1] [...]
	
yum grouplist group1 [...]
	groupinfo
	groupremove group1 [...]
	groupinstall group1 [...]
安装
yum install package1 [package2] [...]
	reinstall	
yum groupinstall group1 [...]


升级
yum update [package1] [package2] [...]

降级
yum downgrade package1 [package2] [...]

检查升级
yum check-update 检查有哪些包可以升级

卸载
yum remove package1 [package2] [...]
	groupremove



yum info PACKAGE
yum search KEYWORD
yum provides KEYWORD
```

```
yum install yum-downloadonly


下载不安装
yum install --downloadonly --downloaddir=<directory> <package>
yum reinstall --downloadonly --downloaddir=<directory> <package>  
```

