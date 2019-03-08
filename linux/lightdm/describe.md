```
grub：引导操作系统
dm: 登录窗口管理，lightdm ,gdm,kdm 等
greeter: lightdm中登录窗口、选择桌面环境
desktop_env: 桌面环境：gnome,deepin,kde,xfc 等
```

grub  + dm+desktop_env :  

```
grub+gdm+gnome       gdm 默认引导gnome。
安装gdm,gnome 后，停用其他dm 服务，开启gdm 服务即可使用。

# systectl enable gdm
```



grub+dm+greeter+desktop_env：

```
grub+lightdm+greeter+deepin/gnome :可引导多种桌面环境
greeter 负责登录窗口及桌面环境选择。

# systectl enable lightdm

lightdm+gnome ： 锁屏不可用
```

/etc/lightdm/lightdm.conf   中配置greeter.

```
[Seat:*]
#greeter-session=lightdm-deepin-greeter
greeter-session=lightdm-webkit2-greeter
```

greeter:

```
​	deepin: lightdm-deepin-greeter
​	lightdm-webkit2-greeter
​	lightdm-gtk-greeter
```

