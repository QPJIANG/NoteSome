```bash
一、安装qemu
sudo pacman -S qemu

其他可选包： 
qemu-arch-extra - 其它架构支持 
qemu-block-gluster - glusterfs block 支持 
qemu-block-iscsi - iSCSI block 支持 
qemu-block-rbd - RBD block 支持 
samba - SMB/CIFS 服务器支持


二、安装libvirt
sudo pacman -S libvirt virt-manager 

为了网络连接，安装这些包：
ebtables 和 dnsmasq 用于默认的 NAT/DHCP网络
bridge-utils 用于桥接网络
openbsd-netcat 通过 SSH 远程管理


启动/开机自起守护进程
systemctl start libvirtd    #启动libvirtd进程
systemctl enable libvirtd   #开机自起


usermod -a -G kvm <user_name> 


----------------------------------------------
hostonly:
虚拟网络：
	lsolated network
	配置ipv4 网段，及dhcp
同时宿主机开启网络转发：
    iptables  -F    （清空iptables）
    编辑/etc/sysctl.conf （root权限,没有该文件就创建）
        取消注释 ： net.ipv4.ip_forward=1 
        执行 ： sudo sysctl -p     此时，网络转发功能应该就开启了

    - 可以使用如下命令验证： cat /proc/sys/net/ipv4/ip_forward 命令返回1，说明网络转发已开启。

    iptables -N fw-open
    iptables -A FORWARD -j fw-open 
    iptables -t nat -A POSTROUTING -o <上外网网卡名> -s 192.168.56.0/24 -j MASQUERADE
```

