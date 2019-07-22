VACUUM

pgsql 磁盘占用较多是,delete 清理数据后,磁盘空间未释放. 需要vacuum 来释放磁盘.

drop 表,磁盘空间会立即释放.



切换数据库管理员，清理指定数据库 (参考： <https://www.cnblogs.com/pengai/p/8073218.html>)

```sql
vacuumdb -d yourdbname -f -z -v 
```





登录数据库：（参考： <https://www.postgresql.org/docs/9.1/sql-vacuum.html>）

```
vacuum full  <table_name>;   清理指定数据表

vacuum full  ;

vacuum ;
```

