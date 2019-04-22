<https://blog.csdn.net/dzjun/article/details/62421718>

```
(1)安装Superset 
pip install superset 
	（配置数据库，创建数据库，数据库用户）

(2)创建管理员用户名和密码 
fabmanager create-admin --app superset 

(3)初始化Superset 
superset db upgrade 

(4)装载初始化样例数据 
superset load_examples 

(5)创建默认角色和权限 
superset init 

(6)启动Superset 
superset runserver 

默认端口：8088
```

