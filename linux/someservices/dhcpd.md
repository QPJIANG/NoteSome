dhcp 介绍：

```
(DynamicHost Configuration Protocol)   动态主机配置协议，是一个局域网的网络协议,使用UDP协议工作。
DHCP有3个端口：
DHCPServer : 67
DHCP Client : 68
546号端口用于DHCPv6 Client
也就是自动的将网路参数正确的分配给网域中的每部电脑，让用户端的电脑可以在开机的时候就立即自动的设定好网路的参数值，这些参数值可以包括了 IP、netmask、network、gateway与 DNS 的位址等等。
```

工作原理：

```
1、寻找server ，client端向局域网发送出一个discover封包;
2、提供IP租用位址，server端收到discover封包后，选择出最前面空置IP，回应给客户端一个offer封包
3、client端收到多台server端offer封包后，挑选最先到达的哪一个offer1，并向局域网发送一个request封包，告之所有server它将指定那一台的IP地址；
4、当server收到request请求封包后，会给客户端一个ACK回应，确认ip租约生效
```



安装:

```
yum search dhcp
yum install dhcp.x86_64 -y
```

配置

```
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp*/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#   “单行配置以 ; 结尾”
option domain-name "server.com";
option domain-name-servers 192.168.3.219;

default-lease-time 600;
max-lease-time 7200;
log-facility local7;
# subnet: 			##指定子网络及子网掩码 
# range: 			## 指定IP范围
# option routers :  ## 指定默认网关

subnet 192.168.3.0 netmask 255.255.255.0 {
	range 192.168.3.100 192.168.3.102;
	option routers 192.168.3.1;
}

```

服务启/停

```
service dhcpd restart/start/stop
or
systemctl stop/start/restart dhcpd
```

