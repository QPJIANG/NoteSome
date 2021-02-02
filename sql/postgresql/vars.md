



```
https://blog.csdn.net/dazuiba008/article/details/79268537



1.psql命令使用变量
表数据如下：
hank=> select * from tb2;
 c1 |  c2   |             c3             
----+-------+----------------------------
  1 | hank  | 2018-02-06 10:08:00.787503
  2 | dazui | 2018-02-06 10:08:08.542481
  3 | wahah | 2018-02-06 10:08:15.468527
  4 | aaaaa | 2018-02-06 10:18:39.289523
 
SQL文本如下
cat  hank.sql 
select * from tb2 where c2=:name and c3>=:time;
通过psql查看
psql -v name="'hank'" -v time="'2018-02-06 10:08:00'" -f hank.sql
 c1 |  c2  |             c3             
----+------+----------------------------
  1 | hank | 2018-02-06 10:08:00.787503
或者
 psql -v name="'hank'" -v time="'2018-02-06 10:08:00'" -c '\i hank.sql'
 c1 |  c2  |             c3             
----+------+----------------------------
  1 | hank | 2018-02-06 10:08:00.787503
 



2.\set使用变量
hank=> \set name hank
hank=> \set time '2018-02-06 10:09:00'   
hank=>  select * from tb2 where c2=:'name' and c3>=:'time';
 c1 |  c2  |             c3             
----+------+----------------------------
  1 | hank | 2018-02-06 10:08:00.787503
  
  
 
3.通过定义参数实现
设置一个session级别的参数，通过current_setting取值
hank=>  set session "asasd.time" to "2018-02-06 10:09:00"; 
SET
hank=>  select * from tb2 where c3 >= current_setting('asasd.time')::timestamp;
 c1 |  c2   |             c3             
----+-------+----------------------------
  4 | aaaaa | 2018-02-06 10:18:39.289523
(1 row)
```

