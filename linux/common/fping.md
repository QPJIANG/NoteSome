```
fping 源码编译：
1. 下载源码并解压
2. 进入解压目录
	./configure
	make
	会在src 目录下生成fping 二进制文件。
	
执行端口扫描时权限错误：can't create socket (must run as root?) : Permission denied
# note: 尝试 sudo setcap cap_net_raw+ep fping  无果

# chown root:root/普通用户 fping
# chmod 6755 fping
# chmod +s fping



fping -i 1  -C 4 -q  -g  net

-q
安静模式，所谓安静就是中途不输出错误信息，直接在结果中显示，输出结构整齐、高效。
-C
这里的“c”是大“C”，输入每个ip探测的次数。
-i
通过-i参数可以修改发包间隔，默认为25毫秒一个探测报文。

```

