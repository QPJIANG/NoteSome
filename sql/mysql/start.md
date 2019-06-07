1. 连接数据库所在服务器
2. 启动数据库服务器进程
     systemctl status mariadb  # 查看数据库服务是否启动
       systemctl stop mariadb    # 停止数据库服务
       systemctl start mariadb   # 启动数据服务
       systemctl restart mariadb   # 重启数据服务

3. 登录数据库服务

  mysql -p -u root  （密码 123456）

4： 查看数据库列表： show databases;
	使用数据库: use database_name
	查看数据表列表: show tables;
	查看表结构： 