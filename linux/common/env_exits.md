引用： https://zhidao.baidu.com/question/2122377445683805787.html

```
//变成if判断不存在变量没有输出
if [ $EEE ];then echo aaa; fi 

if [ $EEE ];then
	echo aaa; 
fi 

变量unset后： 变量不存在。

```

