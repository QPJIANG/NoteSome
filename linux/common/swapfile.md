```

创建交换文件：
dd if=/dev/zero of=/var/swap bs=1024 count=4096000

格式化交换文件：
mkswap /var/swap 

加载交换文件：
swapon /var/swap  

查看交换文件：
swapon -s   或  cat /proc/swaps

卸载交换文件：
swapoff /var/swap
```

