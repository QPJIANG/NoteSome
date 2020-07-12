```
# pacman -S mariadb

# mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

# systemctl start mariadb

# mysql_secure_installation

# systemctl restart mariadb
```



使用二进制包安装：

```
mysql 8.0

https://dev.mysql.com/doc/refman/8.0/en/binary-installation.html 安装文档
https://dev.mysql.com/downloads/mysql/ : 下载地址

添加用户
groupadd mysql
useradd -r -g mysql -s /bin/false mysql

解压二进制包，并命名为mysql. 
如果 /etc/my.cnf  /etc/my.cnf.d 存在，先移走。

bin/mysqld --initialize --user=mysql   ： mysql 目录下会生产data 目录。
同时会打印root 默认随机密码
A temporary password is generated for root@localhost: 后是默认密码



bin/mysql_ssl_rsa_setup  --datadir=<data目录： 默认为/usr/loacl/mysql/data>
bin/mysqld_safe --user=mysql &

编辑： support-files/mysql.server 设置如下内容
basedir=<mysql 根目录>
datadir=<mysql data目录>



修改默认密码(不然进行操作是会报： You must reset your password using ALTER USER statement before executing this statement. 的错误)：

alter user user() identified by "密码";

```



```
mysql 5.7


bin/mysqld --initialize --user=mysql  --datadir=<mysql 数据目录>
```

