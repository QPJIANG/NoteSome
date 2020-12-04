ar -vx   xxxxx.deb && tar zxvf xxx.tar.gz



deb:

```
deb 包结构
.
├── control.tar.gz	（安装控制文件）
├── data.tar.xz   （程序文件，目录从根目录开始组织）
└──debian-binary
```

​	

```
control.tar.gz 中的文件

preinst
在Deb包文件解包之前，将会运行该脚本。许多“preinst”脚本的任务是停止作用于待升级软件包的服务，直到软件包安装或升级完成。

postinst
该脚本的主要任务是完成安装包时的配置工作。许多“postinst”脚本负责执行有关命令为新安装或升级的软件重启服务。

prerm
该脚本负责停止与软件包相关联的daemon服务。它在删除软件包关联文件之前执行。

postrm
该脚本负责修改软件包链接或文件关联，或删除由它创建的文件。
```



```
dpkg lock

# rm /var/lib/dpkg/lock-frontend
```





```
Ubuntu中所有packages的信息都在/var/lib/dpkg/目录下，其中子目录”/var/lib/dpkg/info”用于保存各个软件包的配置文件列表.不同后缀名代表不同类型的文件，如:

.conffiles 记录了软件包的配置文件列表。

.list 保存软件包中的文件列表,用户可以从.list的信息中找到软件包中文件的具体安装位置。

.md5sums 记录了软件包的md5信息，这个信息是用来进行包验证的。

.prerm 脚本在Debian报解包之前运行，主要作用是停止作用于即将升级的软件包的服务,直到软件包安装或升级完成。

.postinst脚本是完成Debian包解开之后的配置工作，通常用于执行所安装软件包相关命令和服务重新启动。

/var/lib/dpkg/available文件的内容是软件包的描述信息，该软件包括当前系统所使用的Debian安装源中的所有软件包,其中包括当前系统中已安装的和未安装的软件包。

命令:

dpkg –l | grep package 查询deb包的详细信息，没有指定包则显示全部已安装包
dpkg -s package 查看已经安装的指定软件包的详细信息
dpkg -L package 列出一个包安装的所有文件清单
dpkg -S file 查看系统中的某个文件属于哪个软件包,搜索已安装的软件包
dpkg -i 安装指定deb包
dpkg -R 后面加上目录名，用于安装该目录下的所有deb安装包
dpkg -r remove，移除某个已安装的软件包
dpkg -P 彻底的卸载，包括软件的配置文件
dpkg -c 查询deb包文件中所包含的文件
dpkg -L 查看系统中安装包的的详细清单，同时执行 -c
```

