dnf  新一代的RPM软件包管理器, 可取代yum.



```
dnf repolist   #列举可用软件库
dnf repolist all #列举软件库，包含可用和不可用的软件库

dnf list # 与yum list 一致
dnf list installed  # 列举已安装的软件
dnf list available

dnf search <package_name>	# 包含该关键字的包，关键字可出现在包描述中

dnf provides <file_name>  # 文件在哪个软件包

dnf info <package_name>  # 软件包的详细信息

dnf install <package_name>  # 与yum install 一致
dnf update <package_name>   # 升级软件包
dnf check-update 	#检查系统中所有软件包的更新

dnf update , dnf upgrade  #升级系统中所有有可用升级的软件包

dnf remove <package_name> ,  dnf erase <package_name> # 卸载
dnf reinstall  <package_name>
dnf autoremove  # 移除孤立的软件包
dnf downgrade  <package_name> #降低特定软件包的版本

dnf clean all  # 与 yum clean all 一致

dnf grouplist # 与yum grouplist 一致
dnf groupinstall <groupname> #与yum groupinstall  一致，组名用引号包起来
dnf groupupdate <groupname> 
dnf groupremove <groupname> 

#从特定的软件包库安装特定的软件
dnf –enablerepo=<repo> install <package_name>

#通过所有可用的软件源将已经安装的所有软件包更新到最新的稳定发行版
dnf distro-sync
```

