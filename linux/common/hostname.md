rhel6:

```
1、临时修改主机名

sudo hostname  lyhost
2、永久修改主机名

vim /etc/sysconfig/network
修改里面的HOSTNAME字段即可，重启后生效。
```

