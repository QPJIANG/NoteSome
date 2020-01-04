问题：

​	系统时间与数据库时间不一致	

```
查系统时间
#date

pg上查询：
select now();
show time zone; 
```

解决办法：

```
查看支持的时区：
select * from pg_timezone_names ;
查询东8区：
select * from pg_timezone_names  where utc_offset='08:00:00';
---------------------------------------------
临时：
set time zone 'PRC';重新查询及时生效

---------------------------------------------
永久：
postgresql.conf配置里修改两项


log_timezone = 'PRC'
timezone = 'PRC'

PRC 可是用 Asia/Shanghai 替换

修改好重启pg或者reload重新查询登录生效
```

