https://www.cnblogs.com/jiaoyiping/p/7191300.html



## 索引类型

PostgreSQL提供了几种索引类型：B-tree，Hash，GiST，SP-GiST，GIN和BRIN。每个索引类型使用不同的算法，适合不同种类的查询。默认情况下，CREATE INDEX命令创建B-tree索引



```
CREATE INDEX <index_name> ON <table_name> (filex);


CONCURRENTLY： 第二索引
CREATE UNIQUE INDEX CONCURRENTLY ON <table_name> USING btree(filex);
```





```
删除索引
ALTER TABLE <table_name>  DROP CONSTRAINT <index_name>;
添加主键
ALTER TABLE <table_name> ADD CONSTRAINT <index_name> primary key (filed1, field2);
```



```
更新已有索引为主键：
ALTER TABLE <table_name> 
ADD CONSTRAINT <index_name> 
PRIMARY KEY USING INDEX <exist_index_name>;
```





```sql
-- 创建序列
 create sequence seq_test_1 INCREMENT by 1 MINVALUE 1 NO MAXVALUE start with 1 ;

--查看序列属性
 \d seq_test_1

-- 查看序列最近使用值
select currval('seq_test_1');

-- 序列重置
select setval('seq_test_1',100); 
alter sequence seq_test_1 restart with 200;

-- 下一个序列值
 select nextval('seq_test_1');
```

