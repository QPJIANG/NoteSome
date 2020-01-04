archlinux

```
安装：

基础包
pacman -S plasma
完整包
pacman -S plasma-meta
最简安装（仅有桌面软件）
pacman -S plasma-desktop

然后是登录管理器SDDM
pacman -S sddm

将SDDM设置为开机自启动
systemctl enable sddm

--------------------------------------------------------

卸载
pacman -Rsc plasma
pacman -Rsc kde-applications

部分应用不会删除：比如kdeconnect

查询孤包选择性删除
pacman -Qdt
```

