```
配置：关闭用户使用密码登陆

# vim /etc/ssh/sshd_config

#禁用密码验证
PasswordAuthentication no  
#打开下面3个的注释。43行
#启用密钥验证
RSAAuthentication yes
PubkeyAuthentication yes
#指定公钥数据库文件
AuthorizedKeysFile  .ssh/authorized_keys

可以用下面命令可以修改（最好用vim手动）：
sed -i "s/^PasswordAuthentication.*/PasswordAuthentication no/g" /etc/ssh/sshd_config
sed -i "s/^#RSAAuthentication.*/RSAAuthentication yes/g" /etc/ssh/sshd_config
sed -i "s/^#PubkeyAuthentication.*/PubkeyAuthentication yes/g" /etc/ssh/sshd_config
sed -i "s/^#AuthorizedKeysFile.*/AuthorizedKeysFile .ssh\/authorized_keys/g" /etc/ssh/sshd_config

重启SSH服务前建议多保留一个会话以防不测
# service sshd restart
```

