rpm -qa |grep vnc

yum install tigervnc-server -y
chkconfig vncserver on


vim /etc/sysconfig/vncservers
按模板编辑如下内容
VNCSERVERS=""           #配置显示号和用户
VNCSERVERARGS[]=""      #配置显示号相关配置

切换用户后执行： vncpasswd

service vncserver restart
