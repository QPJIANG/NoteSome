```
mysql> use mysql;
Database changed
mysql> grant all privileges  on *.* to root@'%' identified by "password";
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;

use mysql;
update user set host = '%' where user = 'root';
```

