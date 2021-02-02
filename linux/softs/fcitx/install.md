sudo apt-get purge fcitx*

//sudo apt-get install fcitx-googlepinyin

sudo apt-get install fcitx  im-config  fcitx-table-all  fcitx-ui-classic

apt-cache search fcitx*
sudo apt-get install fcitx-sunpinyin sunpinyin-utils
sudo apt-get install  fcitx-config-common fcitx-config-gtk

/usr/share/fcitx/skin :skin path

cp skin dir to "/usr/share/fcitx/skin"

${HOME}/.config/fcitx/skin

$  fcitx  : run fc





部分应用不能使用中文输入：

1. 在启动脚本中加入

```
	export XMODIFIERS=@im=fcitx
    export XIM=fcitx
    export XIM_PROGRAM=fcitx
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
```

2. 在profile 中加如上内容，然后通过终端启动

搜狗输入法安装:

参考:<https://www.cnblogs.com/JJUT/p/9956426.html>

```
sudo pacman -S fcitx
sudo pacman -S fcitx-configtool
sudo pacman -S fcitx-gtk2 fcitx-gtk3 fcitx-qt4 fcitx-qt5
sudo pacman -S fcitx-sogoupinyin


~/.xprofile 在其末尾添加以下几行：
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"

```

fcitx-cloudpinyin

 fcitx-configtool

fcitx-googlepinyin







```
搜狗输入法：
sudo pacman -S fcitx-sogoupinyin

.xprofile 内容：
export GTK_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
export QT_IM_MODULE=fcitx
fcitx -d -r --enable sogou-qimpanel


fcitx 添加输入法，重启。


fcitx -d -r --enable sogou-qimpanel (可能搜狗启动有延迟，进入桌面后不能立即使用)

------------------------------------------------------------------------------------
切换搜狗输入法后输入时不显示中文：
$ sogou-qimpanel
sogou-qimpanel: error while loading shared libraries: libfcitx-qt.so.0: cannot open shared object file: No such file or directory

$ pkgfile libfcitx-qt.so.0
archlinuxcn/fcitx-lilydjwg-git

$ sudo pacman -S fcitx-lilydjwg-git
resolving dependencies...
looking for conflicting packages...
:: fcitx-lilydjwg-git and fcitx are in conflict. Remove fcitx? [y/N] y
:: fcitx-lilydjwg-git and fcitx-gtk2 are in conflict. Remove fcitx-gtk2? [y/N] y
:: fcitx-lilydjwg-git and fcitx-gtk3 are in conflict. Remove fcitx-gtk3? [y/N] y

Packages (4) fcitx-4.2.9.7-1 [removal]  fcitx-gtk2-4.2.9.7-1 [removal]  fcitx-gtk3-4.2.9.7-1 [removal]  fcitx-lilydjwg-git-2:4.2.9.7.20191107-1

Total Download Size:    7.14 MiB
Total Installed Size:  35.35 MiB
Net Upgrade Size:       0.48 MiB

:: Proceed with installation? [Y/n] 
:: Retrieving packages...
 。。。。。。。。。。。。。。。。。。。。。。。。。。。
 
```



<https://github.com/gatieme/AderXCoding/tree/master/system/tools/sougoupinyin>

```

方法1
执行如下指令
cd ~/.config
find . -name sogou*
find . -name Sogou*
将两次搜索到的配置文件删除即可.

一般来说, 总共有如下3个文件夹, 全部删除即可

SogouPY、SogouPY.users、sogou-qimpanel
删除这3个文件夹，然后重启搜狗.
------------------------------------------------
方法2：
通过下面的命令重启搜狗输入法，看重启后是否可以正常使用：
killall fcitx
killall sogou-qinpanel
fcitx &
sogou-qinpanel &

```



```
使用sougou, 用  替换 fcitx 包。
```

