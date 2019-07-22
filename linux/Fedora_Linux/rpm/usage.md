参考：https://www.cnblogs.com/xuxiuxiu/p/5740484.html
```
rpm -i   xxx.rpm  :安装rpm 包 ， -ivh   显示进度

rpm  -ivh --test  :  用来检查依赖关系；并不是真正的安装

--relocate    指定安装路径： rpm -ivh --relocate /=/opt/gaim gaim-1.3.0-1.fc4.i386.rpm

rpm  -Uvh xx.rpm：   升级安装

rpm  -Uvh --oldpackage xx.rpm  : 降级

rpm  -qpi   xxx.rpm：查看rpm包  --query--package--install package信息

 rpm -qpR xxx.rpm :查看包依赖关系
 
rpm2cpio file.rpm |cpio -div  ： 从rpm软件包抽取文件，抽取出来的文件就在当用操作目录中的 usr 和etc中
```

```
rpm　--recompile　vim-4.6-4.src.rpm   ＃这个命令会把源代码解包并编译、安装它

rpm　--rebuild　vim-4.6-4.src.rpm　　＃在安装完成后，还会把编译生成的可执行文件重新包装成i386.rpm的RPM软件包。
```

```
rpm -ql packname : 查看安装位置  rpm rpmquery -ql packname
rpm -qi packname： 查看包信息
rpm -qil packname: 查看包信息和安装位置
rpm -qR packname：查看包依赖
rpm -e packname: 卸载，--nodeps 忽略依赖的检查来删除

```

