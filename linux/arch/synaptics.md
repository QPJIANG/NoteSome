触摸板配置：

参考：<https://blog.csdn.net/yangjvn/article/details/47185589>

```
pacman -S xf86-input-synaptics

#file: /etc/X11/xorg.conf.d/*-synaptics.conf
添加配置:
Section "InputClass"
        Identifier "touchpad catchall"
        Driver "synaptics"
        MatchIsTouchpad "on"

        Option "TapButton1" "1"            #单指敲击产生左键事件
        Option "TapButton2" "2"            #双指敲击产生中键事件
        Option "TapButton3" "3"            #三指敲击产生右键事件

        Option "VertEdgeScroll" "on"       #滚动操作：横向、纵向、环形
        Option "VertTwoFingerScroll" "on"
        Option "HorizEdgeScroll" "on"
        Option "HorizTwoFingerScroll" "on"
        Option "CircularScrolling" "on"  
        Option "CircScrollTrigger" "2"

        Option "EmulateTwoFingerMinZ" "40" #精确度
        Option "EmulateTwoFingerMinW" "8"
        Option "CoastingSpeed" "20"        #触发快速滚动的滚动速度

        Option "PalmDetect" "1"            #避免手掌触发触摸板
        Option "PalmMinWidth" "3"          #认定为手掌的最小宽度
        Option "PalmMinZ" "200"            #认定为手掌的最小压力值
EndSection

注销后重新登录
```

触摸板开关：（安装xfce4-notifyd 用于提示）

```
#!/bin/bash
 
status=`synclient -l | grep TouchpadOff | awk '{print $3}'`
if [ $status -eq 0 ]
then
    synclient TouchpadOff=1
    notify-send "Touchpad is disabled!" --icon=$HOME/.icons/myicons/touchpad-disable-icon-th.png
elif [ $status -eq 1 ]
then
    synclient TouchpadOff=0
    notify-send "Touchpad is enabled!" --icon=$HOME/.icons/myicons/touchpad-enable-icon-th.png
fi

```

