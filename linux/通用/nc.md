nc: netcat


扫描通信端口

nc -zvn  ip  port
nc -zv  ip  port

z 参数告诉netcat使用0 IO,连接成功后立即关闭连接， 不进行数据交换
v  详细输出
n 参数告诉netcat 不要使用DNS反向查询IP地址的域名




usage: nc [-46bCDdhjklnrStUuvZz] [-I length] [-i interval] [-O length]
	  [-P proxy_username] [-p source_port] [-q seconds] [-s source]
	  [-T toskeyword] [-V rtable] [-w timeout] [-X proxy_protocol]
	  [-x proxy_address[:port]] [destination] [port]
	Command Summary:
		-4		Use IPv4
		-6		Use IPv6
		-b		Allow broadcast
		-C		Send CRLF as line-ending
		-D		Enable the debug socket option
		-d		Detach from stdin
		-h		This help text
		-I length	TCP receive buffer length
		-i secs		Delay interval for lines sent, ports scanned
		-j		Use jumbo frame
		-k		Keep inbound sockets open for multiple connects
		-l		Listen mode, for inbound connects
		-n		Suppress name/port resolutions
		-O length	TCP send buffer length
		-P proxyuser	Username for proxy authentication
		-p port		Specify local port for remote connects
        	-q secs		quit after EOF on stdin and delay of secs
		-r		Randomize remote ports
		-S		Enable the TCP MD5 signature option
		-s addr		Local source address
		-T toskeyword	Set IP Type of Service
		-t		Answer TELNET negotiation
		-U		Use UNIX domain socket
		-u		UDP mode
		-V rtable	Specify alternate routing table
		-v		Verbose
		-w secs		Timeout for connects and final net reads
		-X proto	Proxy protocol: "4", "5" (SOCKS) or "connect"
		-x addr[:port]	Specify proxy address and port
		-Z		DCCP mode
		-z		Zero-I/O mode [used for scanning]
	Port numbers can be individual or ranges: lo-hi [inclusive]
