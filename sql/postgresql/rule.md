参考 <https://blog.csdn.net/luojinbai/article/details/44903589>

```sql

新版postgres 不使用trigger,使用function

CREATE [ OR REPLACE ] RULE name AS ON event
    TO table_name [ WHERE condition ]
    DO [ ALSO | INSTEAD ] { NOTHING | command | ( command ; command ... ) }
    
    
    
insert  ： new.<字段名>  获取插入数据的值
update	:  new.<字段名>  获取更新数据的值 ， old.<字段名>  获取更新前的值
delete	:  old.<字段名>  获取s删除前前的值



create or replace rule <rule_name>  as on insert to <bind_table> do also insert into <target_table>  (xxx,xxx,...) values(new.<字段名>,new.<字段名>,...);

create or replace rule <rule_name> as on update to <bind_table> do also insert into <target_table> (xxx,xxx,...) values(old.<字段名>,new.<字段名>....);

create or replace rule <rule_name> as on delete to <bind_table> do also insert into <target_table> (xxx,xxx,...)  values(old.<字段名>,old.<字段名>,...);



DROP RULE [ IF EXISTS ] name ON table_name [ CASCADE | RESTRICT ]
```

