<https://blog.csdn.net/duanbiren123/article/details/85955789>

原因： 索引丢失 （成因未知）

解决办法： 重建索引

```
ALTER TABLE <table_name>  DROP CONSTRAINT <index_name>;

ALTER TABLE <table_name> ADD CONSTRAINT <index_name> primary key (filed1, field2);
```





```

```

