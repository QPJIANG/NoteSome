sudo pacman -S nvidia

sudo pacman -S bumblebee

 sudo gpasswd -a username bumblebee 

sudo systemctl enable bumblebeed.service

reboot



<https://www.cnblogs.com/tonyc/p/7732119.html>





/etc/modprobe.d/blacklist

添加： **blacklist nouveau**