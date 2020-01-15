```
/proc/cpuinfo （cpu 静态信息）
/proc/stat   （cpu 使用情况）
/proc/version  (系统内核版本)
/proc/meminfo   (内存使用情况)
/proc/uptime    （系统负载相关）
/proc/loadavg    (load average)
/proc/net/nfsfs/servers  （挂载的nfs 服务器列表）
/proc/net/rpc/nfs
/proc/net/rpc/nfsd
/proc/diskstats  	(磁盘读写)
/proc/partitions	(磁盘分区)
/proc/net/dev	    (网卡流量统计)
/proc/<pid>/stat	(进程信息)
/proc/<pid>/statm	(进程信息)
/proc/<pid>/io	(进程信息)

lsblk: (获取磁盘分区情况)
lsscsi：磁盘信息
lstopo
lspci
lsusbexit
ifstat  -j
```

```
/proc/uptime  

第一列输出的是，系统启动到现在的时间（以秒为单位），这里简记为num1；
第二列输出的是，系统空闲的时间（以秒为单位）,这里简记为num2。
N: 几个逻辑的CPU（包括超线程）
系统的空闲率(%) = num2/(num1*N) 其中N是SMP系统中的CPU个数。

开机时间
date -d "$(awk -F. '{print $1}' /proc/uptime) second ago" +"%Y-%m-%d %H:%M:%S"

运行时间
 cat /proc/uptime| awk -F. '{run_days=$1 / 86400;run_hour=($1 % 86400)/3600;run_minute=($1 % 3600)/60;run_second=$1 % 60;printf("系统已运行：%d天%d时%d分%d秒",run_days,run_hour,run_minute,run_second)}'
系统已运行：0天4时27分10秒
```

```

/proc/loadavg 
前三个数字大家都知道，是1、5、15分钟内的平均进程数（有人认为是系统负荷的百分比，其实不然，有些时候可以看到200甚至更多）。后面两个呢，一个的分子是正在运行的进程数，分母是进程总数；另一个是最近运行的进程ID号。
```



```
/sys/devices/system/cpu/cpu0/cpufreq/   
/sys/class/hwmon
/sys/devices/system/
```



环境变量：XDG_CURRENT_DESKTOP  用户DE



```
gsettings get org.cinnamon.theme name  桌面窗口主题
gsettings get org.cinnamon.desktop.interface gtk-theme
gsettings get org.cinnamon.desktop.interface icon-theme
gsettings get org.cinnamon.desktop.interface font-name

```

disk temp

```
hddtemp 
```

