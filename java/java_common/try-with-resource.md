带资源的try语句（try-with-resource）

```
//可指定多个资源,使用 ";" 分隔多个资源语句，末尾不要 ";"
try(Resource res = xx1;Resource2 res2=xxx2)
{
	work with res
}                                                                        
```

try块退出时，会自动调用res.close()方法，关闭资源。