 8.x--------------
 /var/log/mysqld.log  中查找初始密码

 GRANT ALL PRIVILEGES ON *.* TO root@"%" IDENTIFIED BY "root12345";

 ALTER USER 'root'@'localhost' IDENTIFIED BY 'root@123456';

 


 5.6 ---------------------
 set password=password('123456');
 flush privileges; 

