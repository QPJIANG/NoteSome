服务启停：

    systemctl status service_name
    systemctl start service_name
    systemctl stop service_name
    systemctl restart service_name

开机运行/不运行

    systemctl enable service_name
    systemctl disable service_name

    update-rc.d service_name disable

列举服务：

    systemctl list -units --type=service