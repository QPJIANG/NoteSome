名称：打开控制中心
命令：dbus-send --print-reply --dest=com.deepin.dde.ControlCenter /com/deepin/dde/ControlCenter com.deepin.dde.ControlCenter.Show





```
qdbus 命令包含在 qt5-tools中

窗口左右停放：
https://unix.stackexchange.com/questions/401948/deepin-shortcut-for-docking-window-to-side-corner-of-screen

自定义快捷键
左边命令：（win+left）
qdbus com.deepin.wm /com/deepin/wm com.deepin.wm.TileActiveWindow 1

右边命令：（win+right）
qdbus com.deepin.wm /com/deepin/wm com.deepin.wm.TileActiveWindow 2


max
qdbus com.deepin.wm /com/deepin/wm com.deepin.wm.PerformAction 2

mix
qdbus com.deepin.wm /com/deepin/wm com.deepin.wm.PerformAction 3

win+s
qdbus com.deepin.wm /com/deepin/wm com.deepin.wm.PerformAction 1

win+w
qdbus com.deepin.wm /com/deepin/wm com.deepin.wm.PerformAction 6
qdbus com.deepin.wm /com/deepin/wm com.deepin.wm.PerformAction 7
```

