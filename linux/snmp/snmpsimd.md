Valid tag values and their corresponding ASN.1/SNMP types are:

2 - Integer32
4 - OCTET STRING
5 - NULL
6 - OBJECT IDENTIFIER
64 - IpAddress
65 - Counter32
66 - Gauge32
67 - TimeTicks
68 - Opaque
70 - Counter64

run agent:
snmpsimd.py --data-dir=./data --agent-udpv4-endpoint=127.0.0.1:1024

snmpwalk
 snmpwalk -v2c -c public 127.0.0.1:1024 system
