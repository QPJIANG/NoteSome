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