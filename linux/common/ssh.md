# 软件安装



| 系统   | 软件包  | 备注 |
| ------ | ------- | ---- |
| arch   | openssh |      |
| centos |         |      |
| ubuntu |         |      |



# 使用与配置 



配置文件：

```
/etc/ssh/ssh_config    客户端配置文件
/etc/ssh/sshd_config   服务端配置文件

～/.ssh/config   	客户端用户级别的配置文件    
```

服务端服务：

```
服务名为: sshd
systemctl   status/start/stop/restart sshd
service sshd status/start/stop/restart
```

客户端：

```
连接命令： ssh 

-X   开启图形，允许服务端的图形应用程序投影图像到本地。



ssh 参数不支持直接带密码。 可使用 sshpass
```





# 补充



```
SSH免密码登陆避免首次需要输入yes
ssh -o stricthostkeychecking=no


/etc/ssh/ssh_config文件中的"# StrictHostKeyChecking ask" 为 "StrictHostKeyChecking no"，
sed -i 's/#   StrictHostKeyChecking ask/StrictHostKeyChecking no/' /etc/ssh/ssh_config


警告：POSSIBLE BREAK-IN ATTEMPT
sed -i 's/GSSAPIAuthentication yes/GSSAPIAuthentication no/' /etc/ssh/ssh_config
```





```
ssh 共享回话
配置 ～/.ssh/config

Host *
    ControlMaster auto
    ControlPath ~/.ssh/master-%r@%h:%p

```

