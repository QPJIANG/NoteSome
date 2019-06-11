### falsk appbuilder 权限控制

查询数据库中的所有权限（可通过查询权限相关表获取数据）

```
# db connection session
    sesh = appbuilder.get_session()

    # query
    pvms = sesh.query(ab_models.PermissionView).all()

    for pvm in pvms:
        print(pvm)
```

SecurityManager:

```
# SecurityManager,
# appbuilder 初始化时附带数据库，SecurityManager 封装了权限相关表的操作。
sm = appbuilder.sm

 # sm： SecurityManager 的一些函数
        # role 相关
        # permission 相关
        # user 相关
        # permission_role 相关
        # permission_on_views 相关
        # permission_view_menu 相关
        # views 相关
```

