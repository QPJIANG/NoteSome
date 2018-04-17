--创建用户


    CREATE USER user_name WITH PASSWORD 'password';

--创建数据库并指定用户

    CREATE DATABASE dbname OWNER user_name ENCODING 'UTF8';

--查看数据库列表

    \l
