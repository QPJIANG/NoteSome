__name__
```
1、__name__这个系统变量显示了当前模块执行过程中的名称，如果当前程序运行在这个模块中，__name__ 的名称就是__main__如果不是，则为这个模块的名称。

2、__main__一般作为函数的入口，类似于C语言，尤其在大型工程中，常常有if __name__ == "__main__":来表明整个工程开始运行的入口。
```





### class:

```
参考：https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904

__slots__: 限制实例的属性  __slots__=("xx","xxxx")  设置实例可用的属性
使用的属性在元组范围外，将报错

__str__()返回用户看到的字符串，
__repr__()返回程序开发者看到的字符串

def __iter__(self)  该方法返回一个迭代对象

 def __next__(self) 拿到循环的下一个值，直到遇到StopIteration错误时退出循环

def __getitem__(self, n)  像list那样按照下标取出元素

 def __getattr__(self, attr)，动态返回一个属性值
 
 def __call__(self)：实例本身上调用  ： 实例（） ，callable()函数，我们就可以判断一个对象是否是“可调用”对象
 
 
 
 
 Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
```



#### 元类

```
参考：https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072
type():
	1. 检测类型
	2. 动态创建类
	 def fn(self, name='world'): # 先定义函数
	 	.....
	 类名= type('类名', (object,), dict(hello=fn)) # 创建类
	 
	 type(类名，继承列表元组，函数列表字典)，返回类
	 

metaclass：
	# metaclass是类的模板，所以必须从`type`类型派生
	# 定义mateclass 类，并编写__new__()方法
	def __new__(cls, name, bases, attrs):
		# do something
		return type.__new__(cls, name, bases, attrs)
	接收到的参数依次是：
        当前准备创建的类的对象；
        类的名字；
        类继承的父类集合；
        类的方法集合。

	
	类指定metaclass 参数
```

