# fcitx

	pacman -S  fcitx
	pacman -S  fcitx-im
	pacman -S  fcitx-googlepinyin
	pacman -S fcitx-configtool
	# pacman -S fcitx-sogoupinyin
	pacman -S  fcitx-cloudpinyin
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
	
	-----------------------------------------
	    fail to install rchlinuxcn-keyring
	    pacman -Syu haveged
	    systemctl start haveged
	    systemctl enable haveged
	
	    rm -fr /etc/pacman.d/gnupg
	    pacman-key --init
	    pacman-key --populate archlinux

# google-chrome

	yaourt google-chrome

# shadowsocks-qt5

	yaourt shadowsocks-qt

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

snapd

```
yaourt -S snapd  # 需要从golang.org 下载依赖 （需要搭梯子）
sudo systemctl enable snapd.socket
```
fish
```
pacman  -S  fish        #一个nice UI的shell，用来代替bash                
						tip：使用chsh -l 查看fish的地址，使用chsh -s    /usr/bin/fish来更换用户默认shell
```

```
ifconfig,route在net-tools中
nslookup,dig在dnsutils中
ftp,telnet等在inetutils中
ip命令在iproute2中。   

# pacman -S net-tools dnsutils inetutils iproute2
```





 pacman -Rcns gnome

sudo pacman -Rs $(pacman -Qqdt) 



软件列表

```
unarchiver   解压工具
flatpak      软件管理
pamac-aur    软件管理
yaourt  	 软件管理
yay  	     软件管理
openssh      sshd
fcitx-im	 输入法
flameshot    截图



字体：(fc-cache -vf : 更新字体缓存)
wqy-microhei 
wqy-zenhei

adobe-source-code-pro-fonts
adobe-source-sans-pro-fonts
adobe-source-serif-pro-fonts
adobe-source-han-sans-cn-fonts
adobe-source-han-serif-cn-fonts

noto-fonts 
noto-fonts-cjk

ttf-ubuntu-font-family
ttf-droid

awesome-terminal-fonts
```

