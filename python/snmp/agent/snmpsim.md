```

pip install snmpsim

启动agent:
snmpsimd.py --data-dir = ./data --agent-udpv4-endpoint = 127 .0.0.1：1024

cat ./data/public.snmprec
1 .3.6.1.2.1.1.1.0 | 4 | Linux的2 .6.25.5-SMP SMP周二6月19日 14：58：11 CDT 2007年的i686
1 .3.6.1.2.1.1.2.0 | 6 | 1 .3.6.1.4.1.8072.3.2.10
1 .3.6.1.2.1.1.3.0 | 67 | 233425120 
1 .3.6.1.2.1.2.2.1.6.2 | 4x | 00127962f940
1 .3.6.1.2.1.4.22.1.3.2.192.21.54.7 | 64x | c3dafe61
。。。。。

之后可用snmp 命令获取数据。


从一些现有的SNMP代理生成模拟数据:
snmprec.py --agent-udpv4-endpoint=demo.snmplabs.com --output-file  public.snmprec 

从MIB文件构建模拟数据
mib2dev.py --output-file  public.snmprec --mib-module IF-MIB

snmpsim 自带一些模拟数据
可通过数据库或代码脚本使调用时获得不同的数据。



```

