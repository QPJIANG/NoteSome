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
fcitx-im	 输入法  (fcitx-lilydjwg-git 替换 fcitx-im)
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

```
rdesktop
xfreerdp



可以在系统属性-远程中开启：【允许远程协助连接这台计算机】+【允许远程连接到此计算机】，如果勾选了【仅运行运行使用网络级别身份验证的远程桌面单位计算机连接】，那么 rdesktop 无法连接.
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.
Failed to initialize NLA, do you have correct Kerberos TGT initialized ?
Failed to connect, CredSSP required by server (check if server has disabled old TLS versions, if yes use -V option).

rdesktop一些常用选项：
-u : Windows用户
-p : Windows口令（非PIN）
-g : 窗口大小，如 1366x768
-f :全屏
-a : 色彩深度 ：8, 15, 16, 24, 32
-r sound ：支持声音
-r clipboard：支持剪切板
-r disk： 远程连接时挂载本地文件目录

% rdesktop 192.168.1.6
% rdesktop -u user -p - -f
% rdesktop -u user -p passwd -g 1366x768 -r sound  -a 32 -r clipboard:PRIMARYCLIPBOARD -r disk:MyDir=/mnt/shared 192.168.1.6


-------------------------------------------------------------------------------------
xfreerdp
/v:<server>[:port] 默认端口 3389
/w、/h 窗口大小
/size:<width>x<height> 窗口大小，如 1024x768
/f 全屏
/workarea Use available work area
/bpp:<depth> 色彩深度 
/u:<user>[@<domain>] 
/p:<password>
/d:<domain> 域，可选
+fonts 平滑字体

% xfreerdp /v:192.168.1.6
% xfreerdp /u:user /p:passwd /v:192.168.1.6 /f
% xfreerdp /bpp:32 +fonts /u:user /p:passwd /v:192.168.1.6 /workarea 
% xfreerdp /bpp:32 +clipboard +fonts /u:user /p:passwd /workarea /sound /drive:shared,/mnt/shared /v:192.168.1.6 
% xfreerdp /bpp:32 +clipboard +fonts /u:user /p:passwd /size:1366x768 /sound -v:192.168.1.6:3389
```

