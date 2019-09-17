参考：

<http://www.zsythink.net/archives/1199/>

<https://blog.51cto.com/13677371/2094355>



防火墙服务

```bash
systemctl status iptables.service 
```

```
链：
PREROUTING
INPUT
POSTROUTING
OUTPUT
FORWARD

```

![](../gitresource/iptables_links.png)

![](../gitresource/iptables_links_tables.png)

表：

```
filter表	（实现包过滤）
nat表	（实现网络地址转换）
mangle表	（实现包修改）
raw表	（实现数据跟踪）
这些表具有一定的优先级：**raw-->mangle-->nat-->filter
```



链表：





```
查看
iptables -L

清除
iptables -F
iptables -X 
```

```
动作选项
     ACCEPT          接收数据包
     DROP             丢弃数据包
     REDIRECT      将数据包重新转向到本机或另一台主机的某一个端口，通常功能实现透明代理或对外开放内网的某些服务
     SNAT             源地址转换
     DNAT             目的地址转换
     MASQUERADE       IP伪装
     LOG               日志功能
     
     
-A 增加	-I 插入	-D 删除	-R 替换     
     
iptables [-t 表名] <-A|I|D|R> 链名 [规则编号] [-i|o 网卡名称] [-p 协议类型] [-s 源ip|源子网] [--sport 源端口号] [-d 目的IP|目标子网] [--dport 目标端口号] [-j 动作]     
```



```bash
禁ping
iptables -A INPUT -p icmp --icmp-type 8 -i <网卡名>  -s 0.0.0.0/0 -j DROP
或
iptables -A INPUT -p icmp  --icmp-type 8  -j DROP
```

```
允许合法网段ip接入
iptables -A INPUT -s <10.0.0.0/24> -p  all -j ACCEPT 
```

