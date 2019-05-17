禁用NetworkManager,使用netctl 管理网络.

```bash
sudo systemctl stop NetworkManager
sudo systemctl disable NetworkManager
```

配置netcl:

```bash
cd /etc/netctl
sudo cp examples/ethernet-static ./enp0s25
```

网卡配置示例:

```
Description='enp0s25'
Interface=enp0s25
Connection=ethernet
IP=static
# Address 可配置多个:Address=('192.168.1.23/24' '192.168.1.87/24')
# 192.168.1.23 ip地址
# /24  子网掩码255.255.255.0 
Address=('192.168.1.23/24')
Gateway='192.168.1.1'
DNS=('192.168.1.11' '192.168.1.12')
TimeoutUp=300
TimeoutCarrier=300

```

加载并启用配置:

```
sudo netctl enable enp0s25   # 会生成服务文件,开机启动
sudo netctl start enp0s25
```

其他配置参考 /etc/netctl/examples  下对应的文件来修改

```
wireless-wpa  : wifi 动态ip
wireless-wpa-static : wifi 今天ip
ethernet-dhcp : 有线动态ip

```

