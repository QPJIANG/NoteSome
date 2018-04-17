# install

     rpm -i http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-release-3.4-2.el7.noarch.rpm


     yum install zabbix-server-pgsql zabbix-web-pgsql zabbix-agent


    install postgresql , and import database(/usr/share/doc/zabbix-server-pgsql*/create.sql.gz)

    vi /etc/zabbix/zabbix_server.conf
    DBHost=localhost
    DBName=zabbix
    DBUser=zabbix
    DBPassword=password

    run:
    systemctl start zabbix-server zabbix-agent httpd
    
    run while os up
    systemctl enable zabbix-server zabbix-agent httpd
