安装 virtualbox 后新建虚拟机后不能启动

错误: kernel driver not installed

解决方法：
sudo pacman -Sy linux-headers
sudo /sbin/rcvboxdrv setup


