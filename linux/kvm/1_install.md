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


# 启动管理器
$ virt-manager  
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





```
virtio-win
```

```
$ sudo pacman -S qemu
resolving dependencies...
looking for conflicting packages...

Packages (11) brltty-6.0-8  celt0.5.1-0.5.1.3-4  libcacard-2.7.0-1  liblouis-3.13.0-1  libslirp-4.1.0-1  seabios-1.13.0-1  spice-0.14.2-1  usbredir-0.8.0-1  vde2-2.3.2-13
              virglrenderer-0.8.2-1  qemu-4.2.0-2



$ sudo pacman -S qemu-block-iscsi
resolving dependencies...
looking for conflicting packages...

Packages (2) libiscsi-1.19.0-1  qemu-block-iscsi-4.2.0-2

$ sudo pacman -S qemu-arch-extra
resolving dependencies...
looking for conflicting packages...

Packages (1) qemu-arch-extra-4.2.0-2


$ sudo pacman -S libvirt virt-manager 
resolving dependencies...
looking for conflicting packages...

Packages (20) augeas-1.12.0-1  ceph-libs-14.2.8-1  glusterfs-1:7.3-1  gtk-vnc-1.0.0-1  gtksourceview4-4.6.0-1  liburcu-0.11.0-1  libvirt-glib-3.0.0-1  libvirt-python-5.8.0-3  netcf-0.2.8-7
              oath-toolkit-2.6.2-7  phodav-2.4-1  python-chardet-3.0.4-4  python-idna-2.9-1  python-requests-2.23.0-1  python-urllib3-1.25.8-2  spice-gtk-0.37-1  virt-install-2.2.1-2
              xmlsec-1.2.29-1  libvirt-5.10.0-2  virt-manager-2.2.1-2

```

