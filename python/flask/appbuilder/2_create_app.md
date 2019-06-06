

### 基本命令:  flask fab 可使用命令 fabmanager  替换

fabmanager 为早期版本的命令, 新版本建议使用 flask fab 替换

fabmanager is going to be deprecated in 2.2.X, you can use the same commands on the improved 'flask fab <command>' 



```
flask fab 
Usage: flask fab [OPTIONS] COMMAND [ARGS]...

  FAB flask group commands

Options:
  --help  Show this message and exit.

Commands:
  babel-compile       Babel, Compiles all translations
  babel-extract       Babel, Extracts and updates all messages marked for...
  collect-static      Copies flask-appbuilder static files to your projects...
  create-addon        Create a Skeleton AddOn (needs internet connection to...
  create-admin        Creates an admin user(创建管理员用户)
  create-app          Create a Skeleton application (needs internet...(创建app)
  create-db           Create all your database objects (SQLAlchemy...
  create-permissions  Creates all permissions and add them to the ADMIN...
  create-user         Create a user(创建普通用户)
  list-users          List all users on the database
  list-views          List all registered views
  security-cleanup    Cleanup unused permissions from views and roles.
  security-converge   Converges security deletes...
  version             Flask-AppBuilder package version

```

###　 创建app:

```
$ flask fab create-app

填写相关参数后会根据app name 在当前目录下创建文件夹,存放项目相关文件
flask fab create-app
Your new app name: fab-demo
Your engine type, SQLAlchemy or MongoEngine (SQLAlchemy, MongoEngine) [SQLAlchemy]: 
Downloaded the skeleton app, good coding!

项目基本骨架:

fab-demo
├── app
│   ├── __init__.py 	# 项目入口	
│   ├── models.py		# mode
│   ├── templates		# web 模板
│   │   └── 404.html
│   ├── translations	# 国际化各项语言目录
│   │   └── pt
│   │       └── LC_MESSAGES
│   │           ├── messages.mo
│   │           └── messages.po
│   └── views.py 	# views	
├── babel	# 国际化base
│   ├── babel.cfg
│   └── messages.pot
├── config.py		#配置文件
├── README.rst
└── run.py		#启动文件

```



###　运行

```
$ cd fab-demo

启动方式１：
$ flask run 　（使用5000 端口启动）
启动方式２：
$ python run.py (使用run.py中配置的端口启动: app.run(host="0.0.0.0", port=8080, debug=True))

此时已经可以访问web
```



创建用户: 

```
创建管理员:
执行 flask fab create-admin  或 fabmanager create-admin

创建普通用户:
flask fab create-user 或 fabmanager create-user
```

