关闭selinux:

```
SELinux一共有3种状态，分别是Enforcing，Permissive和Disabled状态。第一种是默认状态，表示强制启用，第二种是宽容的意思，即大部分规则都放行。第三种是禁用，即不设置任何规则。只能通过setenforce命令来设置前面两种状态，而如果想修改为disable状态，需要修改配置文件，同时重启系统。

查看状态：
# getenforce

临时修改：
# setenforce 0    

永久修改：
配置文件：/etc/selinux/config
将  SELINUX=enforcing   改为 SELINUX=disabled
```

