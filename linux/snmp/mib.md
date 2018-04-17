    设置SNMP MIBs
    MIBs默认在系统目录/usr/share/snmp/mibs下，
    添加MIB名称到/etc/snmp/snmp.conf配置文件中（如果不存在则手动新建配置文件），它们将被Net-SNMP进程用来解析trap OID值。
    例：mibs +JUNIPER-MIB:JUNIPER-FABRIC-CHASSIS:BGP4-MIB
