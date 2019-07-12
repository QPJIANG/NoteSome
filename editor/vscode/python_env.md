```
// python路径配置	 
"python.pythonPath": "/................/bin/python",


// python 测试配置(unittest), 将源码目录加大 sys.path 中,避免引入包时报错
"python.testing.unittestArgs": [
	"-v",
	"-s",
	"/xxxx/xxx",
	"-p",
	"*test.py"
],
"python.testing.pyTestEnabled": false,
"python.testing.nosetestsEnabled": false,
"python.testing.unittestEnabled": true,

"python.jediEnabled": true,  //模块自动补全,改动后重新LOAD生效
```

