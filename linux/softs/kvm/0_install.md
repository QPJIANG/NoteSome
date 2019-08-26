参考：<https://blog.csdn.net/sanxinge/article/details/52347998>

```
sudo pacman -S qemu libvirt virt-manager
sudo pacman -S  bridge-utils

# systemctl start libvirtd    #启动libvirtd进程
# systemctl enable libvirtd   #开机自起


添加用户到kvm用户组 
usermod -a -G kvm <user_name>
```

