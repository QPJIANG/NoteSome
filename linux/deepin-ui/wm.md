```
#!/bin/bash

if [ "$1" == "wm" ];then
	echo "deepin-wm窗管，取代正在运行的窗管"
    deepin-wm --replace &
    exit 0
fi

if [ "$1" == "on" ];then
	echo "开启 metacity 窗管合成，取代正在运行的窗管"
    deepin-metacity --composite --replace &
    exit 0
fi

if [ "$1" == "off" ];then
	echo "关闭 metacity 窗管合成，取代正在运行的窗管"
    deepin-metacity --no-composite --replace &
    exit 0
fi

```

