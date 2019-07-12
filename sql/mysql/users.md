```
mysql> use mysql;
Database changed
mysql> grant all privileges  on *.* to root@'%' identified by "password";
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;

use mysql;
update user set host = '%' where user = 'root';
```

```
参考： https://www.cnblogs.com/sos-blue/p/6852945.html

CREATE USER 'username'@'host' IDENTIFIED BY 'password';
eg:
CREATE USER 'dog'@'localhost' IDENTIFIED BY '123456';
CREATE USER 'pig'@'192.168.1.101_' IDENDIFIED BY '123456';
CREATE USER 'pig'@'%' IDENTIFIED BY '123456';
CREATE USER 'pig'@'%' IDENTIFIED BY '';
CREATE USER 'pig'@'%';


GRANT privileges ON databasename.tablename TO 'username'@'host'
privileges：用户的操作权限，如SELECT，INSERT，UPDATE等，如果要授予所的权限则使用ALL
eg:
GRANT SELECT, INSERT ON test.user TO 'pig'@'%';
GRANT ALL ON *.* TO 'pig'@'%';
GRANT ALL ON maindataplus.* TO 'pig'@'%';

REVOKE privilege ON databasename.tablename FROM 'username'@'host';


SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');

前登陆用户: SET PASSWORD = PASSWORD("newpassword");

DROP USER 'username'@'host';

```

```
参考：
https://www.cnblogs.com/janken/p/5500320.html
1、create schema [数据库名称] default character set utf8 collate utf8_general_ci;--创建数据库

　　采用create schema和create database创建数据库的效果一样。

2、create user '[用户名称]'@'%' identified by '[用户密码]';--创建用户

　　密码8位以上，包括：大写字母、小写字母、数字、特殊字符

　　%：匹配所有主机，该地方还可以设置成‘localhost’，代表只能本地访问，例如root账户默认为‘localhost‘

3、grant select,insert,update,delete,create on [数据库名称].* to [用户名称];--用户授权数据库

　　*代表整个数据库

4、flush  privileges ;--立即启用修改

5、revoke all on *.* from tester;--取消用户所有数据库（表）的所有权限

6、delete from mysql.user where user='tester';--删除用户

7、drop database [schema名称|数据库名称];--删除数据库
```





忘记密码：

[mysqld]后面任意一行添加 skip-grant-tables

重启MySQL

```sql
 use mysql;
 update user set password=password("你的新密码") where user="root";
 flush privileges;
 quit
```



root用户权限丢失：

```sql
[mysqld]后面任意一行添加 skip-grant-tables ， 重启

UPDATE mysql.user SET Grant_priv='Y', Super_priv='Y' WHERE User='root';

FLUSH PRIVILEGES;

GRANT ALL ON *.* TO 'root'@'localhost';

select * from mysql.user

```



mysql.user  密码字段需要为加密字符串。

非加密字符串时：

mysql -h 127.0.0.1 -P 端口 -u root@非加盟密码   登录

