install nemo

创建nemo.desktop文件，将文件复制到~/.config/autostart目录下，内容如下：

> [Desktop Entry]
> Type=Application
> Name=Desktop Icons
> Exec=nemo-desktop
> OnlyShowIn=GNOME;
> NoDisplay=true
> X-GNOME-Autostart-Phase=Desktop
> X-GNOME-Autostart-Notify=true
> X-GNOME-AutoRestart=true
> X-GNOME-Provides=filemanager

显示桌面图标

> gsettings set org.nemo.desktop show-desktop-icons true

注销账户重新登陆





```
nemo

安装完成，设置Nemo作为默认的文件管理器，并让 nemo 处理桌面图标：

xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search

gsettings set org.gnome.desktop.background show-desktop-icons false
gsettings set org.nemo.desktop show-desktop-icons true
 

恢复原来设置：

xdg-mime default nautilus.desktop inode/directory application/x-gnome-saved-search

gsettings set org.nemo.desktop show-desktop-icons false
gsettings set org.gnome.desktop.background show-desktop-icons true
```

