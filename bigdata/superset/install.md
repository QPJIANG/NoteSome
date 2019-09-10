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





```
python 3.7	+	supserset 0.28.1


# Install superset
pip install superset

# Initialize the database
superset db upgrade

# Create an admin user (you will be prompted to set a username, first and last name before setting a password)
$ export FLASK_APP=superset
flask fab create-admin

# Load some data to play with
superset load_examples

# Create default roles and permissions
superset init

# To start a development web server on port 8088, use -p to bind to another port
superset run -p 8080 --with-threads --reload --debugger

---------------------------------------------------------------------------------





cannot import name '_maybe_box_datetimelike' from 'pandas.core.common'
pip install pandas==0.23.4

pip install flask==1.0

sqlalchemy.exc.InvalidRequestError: Can't determine which FROM clause to join from, 
pip install SQLAlchemy==1.2.18
```

