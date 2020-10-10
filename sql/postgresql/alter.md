

```
修改字段类型，或长度

alter table <表名> alter column <列名> type <新类型>;
```

```
添加列

ALTER TABLE <表名>  ADD   <列名> <类型>
```

```
删除列

ALTER TABLE <表名>  DROP COLUMN <列名>;
```

```
设置not null

ALTER TABLE table_name MODIFY column_name datatype NOT NULL;
```

```
添加unique 约束

ALTER TABLE table_name
ADD CONSTRAINT MyUniqueConstraint UNIQUE(column1, column2...);

```

```
添加检查约束

ALTER TABLE table_name
ADD CONSTRAINT MyCheckConstraint CHECK (CONDITION);
```

```
添加主键约束

ALTER TABLE table_name
ADD CONSTRAINT MyPrimaryKey PRIMARY KEY (column1, column2...);
```

```
删除约束

ALTER TABLE table_name
DROP CONSTRAINT MyConstraint;


```

