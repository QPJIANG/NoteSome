参考： 

https://blog.csdn.net/u010251897/article/details/80136995

https://www.jianshu.com/p/705c359ed76e



```
创建主表：

创建分区表：
CREATE TABLE 分表名 () inherits (主表名);  

create table 分表名 (
    check ( 时间字段名 >= date '2018-01-01' and 时间字段名 < date '2018-04-01')
) inherits (主表名);


创建触发器或rule：

挂载触发器（RULE 可在创建时绑定触发条件）：

```

pg11: 

参考：  http://www.cnblogs.com/jonney-wang/p/9238923.html

​		http://www.postgres.cn/news/viewone/1/271

```
range分区表：

create table 主表名(...) PARTITION BY RANGE (时间字段) WITH (OIDS = FALSE） ;
分区主表不能建立全局约束，使用partition by range(xxx)说明分区的方式，xxx可以是多个字段


CREATE TABLE 分表名  PARTITION OF 主表名 FOR VALUES FROM ('2017-01-01 00:00:00') TO ('2018-01-01 00:00:00');

list分区表：
create table 主表名(...) partition by list( xxx );
CREATE TABLE 分表名  PARTITION OF 主表名 FOR VALUES in ('xx')
```



