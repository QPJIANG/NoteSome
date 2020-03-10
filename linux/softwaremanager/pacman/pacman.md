pacman 用法：

```
    pacman -Sy abc                 #和源同步后安装名为abc的包
pacman -S   abc                    #从本地数据库中得到abc的信息，下载安装abc包
    pacman -Sf abc                 #强制安装包abc
    pacman -Ss abc                 #搜索有关abc信息的包
    pacman -Si abc                 #从数据库中搜索包abc的信息
    pacman -Qi abc                 #列出已安装的包abc的详细信息
    pacman -Qii package_name       #使用两个 -i 将同时显示备份文件和修改状态
    pacman -Qk package_name   	   #检查软件包安装的文件是否都存在
pacman -Ql package_name   		   #要获取已安装软件包所包含文件的列表
pacman -Syu                        #同步源，并更新系统
    pacman -Sy                     #仅同步源
    pacman -Su                     #更新系统
pacman -R   abc                #删除abc包
    pacman -Rc abc             #删除abc包和依赖abc的包
    pacman -Rn package_name
pacman -Rsc abc                #删除abc包和abc依赖的包
pacman -Rdd package_name       #要删除软件包，但是不删除依赖这个软件包的其他程序

	pacman -Sc                 #清理/var/cache/pacman/pkg目录下的旧包
pacman -Scc                    #清除所有下载的包和数据库
pacman -U   abc                #安装下载的abs包，或新编译的abc包
    pacman -Sd abc             #忽略依赖性问题，安装包abc
    pacman pacman -Su --ignore foo   #升级时不升级包foo
    pacman -Sg abc             #查询abc这个包组包含的软件包
pacman -Sw abc				   # 下载包而不安装
    pactree package_name       #要显示软件包的依赖树
    pactree -r package_name    #检查一个安装的软件包被那些包依赖
pacman -Qdt   				   #罗列所有不再作为依赖的软件包(孤立orphans)
pacman -Qet   				   #罗列所有明确安装而且不被其它包依赖的软件包
```







官方仓库：	

```

```

非官方仓库：

```
参考： https://wiki.archlinux.org/index.php/Unofficial_user_repositories
分为签名的和未签名的仓库。

```





















