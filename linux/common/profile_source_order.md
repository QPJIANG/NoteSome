系统登录顺序：

/etc/profile

/etc/profile.d/a.sh (a.sh自己建的)

/root/.bash_profile

/root/.bashrc

/etc/bashrc

 

/bin/bash 提供命令解释器（终端）

直接打/bin/bash 非登录shell

/root/.bashrc

/etc/bashrc

/etc/profile.d/a

 

可将别名alias等写入以上三个文件



bash  如何获取当前文件的绝对路径

```
#!/bin/bash
CURRENT_DIR=$(cd `dirname $0`;pwd)
echo $CURRENT_DIR
```



source 文件获取当前文件的绝对路径 

```
#!/bin/bash
cd $(dirname $BASH_SOURCE)
CURRENT_DIR=$(pwd)
echo $CURRENT_DIR
```

