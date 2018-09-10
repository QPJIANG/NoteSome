http://blog.csdn.net/hawkdowen/article/details/38357771

1. vbox全局设置
新建host-only网络。一般网络名会是vboxnet0，默认IP地址为192.168.56.1(可以自定义)，子网掩码:255.255.255.0。
dhcp 可以选择性开启

2. 虚拟机网卡选择host-only,界面名称 选择步骤1 的网络

3. 虚拟机配置好网络

4. ubuntu 开启网络转发

5. 
编辑/etc/sysctl.conf （root权限）
取消注释 ： net.ipv4.ip_forward=1 
执行 ： sudo sysctl -p     此时，网络转发功能应该就开启了
可以使用如下命令验证： cat /proc/sys/net/ipv4/ip_forward 命令返回1，说明网络转发已开启。
配置网络转发规则： 
sudo iptables -t nat -A POSTROUTING -o eth0 -s 192.168.56.0/24 -j MASQUERADE
        eth0 改为上网的网卡， 192.168.56.0 改为上网的网段
        sudo iptables -t nat -A POSTROUTING -o wlp6s0 -s 192.168.4.0/24 -j MASQUERADE


配置网络转发规则（临时生效）可以把 
iptables -t nat -A POSTROUTING -o wlp6s0 -s 192.168.4.0/24 -j MASQUERADE 
加入到 /etc/rc.local  使其开机生效
有多个网卡可以加多条



linux 虚拟机IP配置：
IPADDR=192.168.4.30
NETMASK=255.255.255.0
GATEWAY=192.168.4.1
DNS1=192.168.2.1
DNS2=192.168.1.1
NAME="enp0s3"
DEVICE="enp0s3"
ONBOOT="yes"    

 2note:ip配置文件末尾不要有空行





Arch:

启动firewall: systemctl  entable/start iptables

```
编辑/etc/sysctl.conf （root权限）
    取消注释 ： net.ipv4.ip_forward=1 
    执行 ： sudo sysctl -p     此时，网络转发功能应该就开启了
   
* 可以使用如下命令验证： cat /proc/sys/net/ipv4/ip_forward 命令返回1，说明网络转发已开启。

iptables -N fw-open
iptables -A FORWARD -j fw-open 
iptables -t nat -A POSTROUTING -o wlp3s0 -s 192.168.56.0/24 -j MASQUERADE
```

