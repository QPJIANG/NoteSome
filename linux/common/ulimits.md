资源使用限制

参考： <https://www.cnblogs.com/operationhome/p/11966041.html>

```
ulimit -a

ulimit <选项>  		 # 查看
ulimit <选项> <limit>  # 修改



输出样例：
core file size          (blocks, -c) unlimited
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 63377
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 63377
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited

```

```
配置文件： /etc/security/limits.conf
配置后新启终端生效（或reboot,重启sshd）
```

```
配置说明

# 第一列表示用户,组（@开头）
# 第二列表示软限制还是硬限制
# 第三列表示限制的资源类型
# 第四列表示限制的最大值

# hard和soft的区别： 
# soft是一个警告值，而hard则是一个真正意义的阀值，超过就会报错，一般情况下都是设为同一个值。

# core是内核文件
# nofile是文件描述符
# noproc是进程
# 一般情况下只限制文件描述符数和进程数就够了



# 打开文件数
* soft nofile 65536      # open files  (-n)
* hard nofile 65536

# 进程数 
* soft nproc 65565
* hard nproc 65565       # max user processes   (-u)

*        soft    memlock        unlimited
*        hard    memlock        unlimited
```

