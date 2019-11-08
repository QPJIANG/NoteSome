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

