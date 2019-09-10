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

