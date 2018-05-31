数据类型
```
String
Hash
List
Set
Zset
```

String:
```
	set key value
	get key
	del key
```
Hash:
```
	HMSET mainkey key1 value1 key2 vaue2
	HGET mainkey key1
	HGET mainkey key2	
	HGETALL mainkey
```
List:
```
	lpush key value
	lrange key start end
	lindex key index
	len key
	lpop key
	lset key index value
	ltrim keys start stop    (ltrim key 1 0  : empty the list)
```
Set:
```
sadd key value1
sadd key value2
smembers key
```
Zset:
```
zadd key score member 
ZRANGEBYSCORE key  start end
```