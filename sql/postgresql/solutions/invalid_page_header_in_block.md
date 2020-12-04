

参考：

```
https://lxadm.com/PostgreSQL:_ERROR:_invalid_page_header_in_block_13760_of_relation_base/16995/67484
```



```
# SET zero_damaged_pages = on;
# VACUUM FULL damaged_table;
# reindex table damaged_table;
```



单个分区表受损也可能导致主表查询报错： 此时需要对分区表进行处理。

