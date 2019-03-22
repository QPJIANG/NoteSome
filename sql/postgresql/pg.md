```
table: pg_user 数据库用户
 usename  用户名
 usesysid  用户id
 | usecreatedb  是否有创建数据库的权限：t/f
 | usesuper 是否是超级用户: t/f
 userepl  | usebypassrls 
 passwd    # 密码********， 不可见
 valuntil | useconfig 
 
 
```

```
table pg_database: 数据库列表

select datname,datdba from pg_database ;
datname 数据库名：
datdba 用户id
```

```
pg_aggregate                    pg_index                        pg_sequence                     pg_statio_sys_sequences        
pg_am                           pg_indexes                      pg_sequences                    pg_statio_sys_tables           
pg_amop                         pg_inherits                     pg_settings                     pg_statio_user_indexes         
pg_amproc                       pg_init_privs                   pg_shadow                       pg_statio_user_sequences       
pg_attrdef                      pg_language                     pg_shdepend                     pg_statio_user_tables          
pg_attribute                    pg_largeobject                  pg_shdescription                pg_statistic                   
pg_auth_members                 pg_largeobject_metadata         pg_shseclabel                   pg_statistic_ext               
pg_authid                       pg_locks                        pg_stat_activity                pg_stats                       
pg_available_extension_versions pg_matviews                     pg_stat_all_indexes             pg_subscription                
pg_available_extensions         pg_namespace                    pg_stat_all_tables              pg_subscription_rel            
pg_cast                         pg_opclass                      pg_stat_archiver                pg_tables                      
pg_catalog.                     pg_operator                     pg_stat_bgwriter                pg_tablespace                  
pg_class                        pg_opfamily                     pg_stat_database                pg_temp_1.                     
pg_collation                    pg_partitioned_table            pg_stat_database_conflicts      pg_timezone_abbrevs            
pg_config                       pg_pltemplate                   pg_stat_progress_vacuum         pg_timezone_names              
pg_constraint                   pg_policies                     pg_stat_replication             pg_toast.                      
pg_conversion                   pg_policy                       pg_stat_ssl                     pg_toast_temp_1.               
pg_cursors                      pg_prepared_statements          pg_stat_subscription            pg_transform                   
pg_database                     pg_prepared_xacts               pg_stat_sys_indexes             pg_trigger                     
pg_db_role_setting              pg_proc                         pg_stat_sys_tables              pg_ts_config                   
pg_default_acl                  pg_publication                  pg_stat_user_functions          pg_ts_config_map               
pg_depend                       pg_publication_rel              pg_stat_user_indexes            pg_ts_dict                     
pg_description                  pg_publication_tables           pg_stat_user_tables             pg_ts_parser                   
pg_enum                         pg_range                        pg_stat_wal_receiver            pg_ts_template                 
pg_event_trigger                pg_replication_origin           pg_stat_xact_all_tables         pg_type                        
pg_extension                    pg_replication_origin_status    pg_stat_xact_sys_tables         pg_user                        
pg_file_settings                pg_replication_slots            pg_stat_xact_user_functions     pg_user_mapping                
pg_foreign_data_wrapper         pg_rewrite                      pg_stat_xact_user_tables        pg_user_mappings               
pg_foreign_server               pg_roles                        pg_statio_all_indexes           pg_views                       
pg_foreign_table                pg_rules                        pg_statio_all_sequences        
pg_group                        pg_seclabel                     pg_statio_all_tables           
pg_hba_file_rules               pg_seclabels                    pg_statio_sys_indexes  
```



pg_rules，pg_tables:  查询结果与当前数据库相关。

