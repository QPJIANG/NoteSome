```
双屏配置：xrander ,arandr (图像配置工具)


```

lock  ~/.config/i3/config:

```


# i3lock
mode "i3lock: Return to lock/Escape to Cancel" {
        bindsym Return mode "default" exec i3lock -i ~/Pictures/Wallpapers/x.png
        bindsym Escape mode "default" 
}

bindsym Control+$ALT +l mode "i3lock: Return to lock/Escape to Cancel"


```

```
xcompmgr  用来实现终端透明
volumeicon
feh	  用于设置背景图


# Autostart
exec --no-startup-id xcompmgr &
# exec --no-startup-id nm-applet  管理网络 （托盘）
exec --no-startup-id fcitx
exec --no-startup-id volumeicon  控制音量的小插件(托盘)


lxappearance 用来调节gtk主题和字体
dunst  系统通知
```



```
https://www.jianshu.com/p/e1184c26794b

```



```
rofi 替换启动器

bindsym $mod+d exec --no-startup-id "rofi -combi-modi window,drun,run,ssh -show combi -modi combi"
```



```
xprop
获取窗口class
```

