```
tzselect
```

```
软连接 或复制文件覆盖/etc/localtime
/etc/localtime -> /usr/share/zoneinfo/Asia/Shanghai  
```

```
timedatectl 查看时间各种状态
timedatectl list-timezones: 列出所有时区
timedatectl set-local-rtc 1 将硬件时钟调整为与本地时钟一致, 0 为设置为 UTC 时间
timedatectl set-timezone Asia/Shanghai 设置系统时区为上海
```

```
profile 文件：配置TZ 环境变量

TZ='Asia/Shanghai'
export TZ
```



------------------------------------

```
# date -s 11/14/2018  ## 月/日/年
# date -s 10:48:50    ## 十分秒
# 
# hwclock --systohc  ##使用系统时间同步硬件时间
# hwclock ## 查看硬件时间
```

```
# hwclock --set --date="11/14/2018 10:56:35"  ## 设置硬件时间
# hwclock --hctosys  ##使用硬件时间同步系统时间
```

```
# hwclock  --show 
# clock  --show
# hwclock
# clock
## 等价命令
## clock 与hwclock  用法基本等价
```

