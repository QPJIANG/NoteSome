```
#: 以管理员身份运行

能ping通dns, 但无法解析域名
# netsh winsock reset catalog



重启网络（禁用网卡，启用网卡）：
netsh interface set interface 网卡名 disabled
netsh interface set interface 网卡名 enabled
eg:
# netsh interface set interface 以太网 disabled
# netsh interface set interface 以太网 enabled
```

