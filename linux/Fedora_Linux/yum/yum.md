软件安装：

``` bash
参考： http://man.linuxde.net/yum
# yum install -y <packname>


install：安装rpm软件包；
update：更新rpm软件包；
check-update：检查是否有可用的更新rpm软件包；
remove：删除指定的rpm软件包；
list：显示软件包的信息；
search：检查软件包的信息；
info：显示指定的rpm软件包的描述信息和概要信息；
clean：清理yum过期的缓存；
shell：进入yum的shell提示符；
resolvedep：显示rpm软件包的依赖关系；
localinstall：安装本地的rpm软件包；
localupdate：显示本地rpm软件包进行更新；
deplist：显示rpm软件包的所有依赖关系。

yum --help: 查看所有参数
```


下载不安装:
```
参考：https://www.cnblogs.com/wangmo/p/7205528.html

# yum install -y yum-utils 

# yumdownloader <package-name> 

resolve下载依赖
# yumdownloader <package-name> --resolve 

yum install --downloadonly --downloaddir=/tmp <package-name> 
```


```
检查包是否安装
yum list installed <packname> 
```





yum 源：

```
http://mirrors.163.com/.help/centos.html
http://mirrors.ustc.edu.cn/help/
```

