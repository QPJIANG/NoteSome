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
	
运行级别
参考：https://blog.csdn.net/u012486840/article/details/53161574
``` stylus
	init级别		systemctl target
	0		shutdown.target
	1		emergency.target
	2		rescure.target
	3		multi-user.target
	4		无
	5		graphical.target
	6		无
	systemctl命令					说明
	systemctl get-default				获得当前的运行级别
	systemctl set-default multi-user.target		设置默认的运行级别为mulit-user
	systemctl isolate multi-user.target		在不重启的情况下，切换到运行级别mulit-user下
	systemctl isolate graphical.target		在不重启的情况下，切换到图形界面下

```


