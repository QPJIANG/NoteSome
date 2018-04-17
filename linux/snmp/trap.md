# config

    在snmptrapd.conf中加入以下指令：
    authCommunity log,execute,net public
    这条指令指明以“public”为“community”请求的snmp “notification”允许的操作。
    各变量意义如下：
    log: log the details of the notification - either in a  specified file, to standard output (or stderr), or via syslog(or similar).
    execute: pass the details of the trap to a specified handler program, including embedded perl.
    net: forward the trap to another notification receiver.

    若想对接收到的信息进行处理，可以使用traphandle，示例如下：
    traphandle SNMPv2-MIB::coldStart    /usr/nba/bin/traps cold
    traphandle SNMPv2-MIB::warmStart    /usr/nba/bin/traps warm
    traphandle IF-MIB::linkDown         /usr/nba/bin/traps down
    traphandle IF-MIB::linkUp           /usr/nba/bin/traps up
    第一个参数为从snmptrapd接收的OID，第二个参数为调用的程序。此系统未做traphandle处理。

    conf.example:

    disableAuthorization yes
    traphandle default  /opt/test/trapcaller.sh
    authCommunity   execute public

    #traphandle SNMPv2-MIB::sysLocation.0     /opt/test/lognotify
    #traphandle SNMPv2-MIB::coldStart /opt/test/lognotify.sh    cold
    #traphandle default /usr/sbin/snmptthandler
    #traphandle 1.3.6.1.4.1.2345  /opt/test/lognotify.sh
    #traphandle default  /opt/test/lognotify.sh
    #traphandle default  /opt/test/traphandle.pel
    #traphandle default  /opt/test/traphandle.py
    #authCommunity   log,execute,net public
    authCommunity   execute public
    #ignoreauthfailure  yes



    runtrap reserver:
    snmptrapd  -c snmptrapd.conf -f -Le -d  
    注意：
      不带-c,加载默认配置/etc/snmp/snmptrapd.conf
      -c 会同时加载/etc/snmp/snmptrapd.conf 和 ./snmptrapd.conf ， 如果这两个文件是同一个，handle会调两次

    snmptrapd  -f -Le -d  
    snmptrapd  -c snmptrapd.conf -f  -d -Dread_config  ： 查看配置加载情况



## usage
    exmaple:
    snmptrap -v 2c -c public 10.10.12.219 "aaa" 1.3.6.1.4.1.2345 SNMPv2-MIB::sysLocation.0 s "just here"
    snmptrap -m ./sample-trap.mib -v 2c -c public 16.157.76.227:162  "" IBM-DW-SAMPLE::nodeDown IBM-DW-SAMPLE::nodeDown.1 s "M1"

    snmptrap        命令
    -v 2c           Snmp协议版本
    -c public       共同体
    10.10.12.219    snmp代理的IP
    "aaa"           主机名称, 可以为空
    1.3.6.1.4.1.2345    Enterprise-OID
    SNMPv2-MIB::sysLocation.0   数据OID
    s                   数据类型
    "This is a test"    数据值

    snmptrap -v 2c -c public agent_ip  "" 1.3.6.1.4.1.2345 SNMPv2-MIB::sysLocation.0 s "just here"
    snmptrap -v 2c -c public agent_ip "" coldStart

    snmptrap enterpriseOID(generic OID) OID(subOID) type value

    The TYPE is a single character, one of:
    i INTEGER
    u UNSIGNED
    c COUNTER32
    s STRING
    x HEX STRING
    d DECIMAL STRING
    n NULLOBJ
    o OBJID
    t TIMETICKS
    a IPADDRESS
    b BITS
