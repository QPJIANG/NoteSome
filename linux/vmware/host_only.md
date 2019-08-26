



root:

```
iptables  -F    
编辑/etc/sysctl.conf （root权限）
    取消注释 ： net.ipv4.ip_forward=1 
    执行 ： sudo sysctl -p     此时，网络转发功能应该就开启了

- 可以使用如下命令验证： cat /proc/sys/net/ipv4/ip_forward 命令返回1，说明网络转发已开启。

iptables -N fw-open
iptables -A FORWARD -j fw-open 
iptables -t nat -A POSTROUTING -o wlp3s0 -s 192.168.56.0/24 -j MASQUERADE
```

