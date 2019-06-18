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