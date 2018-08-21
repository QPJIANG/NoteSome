 Parsing error: x-invalid-end-tag
 
 参考：https://blog.csdn.net/zy13608089849/article/details/79545738
 
解决方案

``` 
修改配置文件，忽略该项检查：

根目录下 - .eslintrc.js - rules
```


添加一行：

``` 
 "vue/no-parsing-error": [2, { "x-invalid-end-tag": false }]
```
