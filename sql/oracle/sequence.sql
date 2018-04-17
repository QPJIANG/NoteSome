-- create sequence
CREATE SEQUENCE seq_name MINVALUE 1 NOMAXVALUE INCREMENT BY 1 START WITH 1 NOCACHE;

-- get value
SELECT seq_name.nextval from dual;

-- table 字段递增 通过 触发器+sequence 实现