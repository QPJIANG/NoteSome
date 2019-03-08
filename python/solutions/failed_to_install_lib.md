```
MySQL-python-1.2.5 will not compile against MariaDB 10.2 (libmariadb-dev)

error:
	_mysql.c:2005:41: error: ‘MYSQL’ {aka ‘struct st_mysql’} has no member named ‘reconnect’

solution:
	https://github.com/DefectDojo/django-DefectDojo/issues/407	
	$ sudo sed '/st_mysql_options options;/a unsigned int reconnect;' /usr/include/mysql/mysql.h -i.bkp
	
```

