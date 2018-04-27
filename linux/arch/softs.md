# fcitx

	pacman -S  fcitx
	pacman -S  fcitx-im
	pacman -S  fcitx-googlepinyin
	
	~/.xprofile
	export LC_ALL=zh_CN.UTF-8
	export GTK_IM_MODULE=fcitx
	export QT_IM_MODULE=fcitx
	export XMODIFIERS="@im=fcitx"
	
	(reboot)
# notepadqq

	pacman -S notepadqq

# source

	在 /etc/pacman.conf 文件末尾添加两行：
	
	[archlinuxcn]
	Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
	
	然后请安装 archlinuxcn-keyring 包以导入 GPG key。
	
	pacman -Syu
	pacman -S yaourt

# google-chrome

	yaourt google-chrome

# shadowsocks-qt5

	yaourt shadowsock

# remmina

	pacman -S remmina
	
	yaourt remmina-plugin-rdesktop

# conky

	# pacman -S  conky
	# pacman -S  conky-manager

pamac-aur

```
# pacman -S pamac-aur
```

Typora

```
yaourt Typora
```

