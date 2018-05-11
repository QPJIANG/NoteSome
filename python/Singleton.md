单例：

1. 装饰器
```
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Foo(object):
    pass
    
 
@singleton
class Foo(object):
    pass
foo1 = Foo()

#等同于
class Foo(object):
    pass
foo1 = singleton(Foo)

```
2. 重写 __new__
```
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, 
                cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Foo(Singleton):
    pass
```

3.  __metaclass__
```
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        print 'call Singleton __call__'
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, 
                                  cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(object):
    __metaclass__ = Singleton
```

4. 模块

   单例对象在模块的 __init__.py 中 ，引入模块时，引入该单例对象

5. 在类方法生成单例

   ```
   import time
   import threading
   class Singleton(object):
       _instance_lock = threading.Lock()
   
       def __init__(self):
           time.sleep(1)
   
       @classmethod
       def instance(cls, *args, **kwargs):
           with Singleton._instance_lock:
               if not hasattr(Singleton, "_instance"):
                   Singleton._instance = Singleton(*args, **kwargs)
           return Singleton._instance
   
   
   def task(arg):
       obj = Singleton.instance()
       print(obj)
   for i in range(10):
       t = threading.Thread(target=task,args=[i,])
       t.start()
   ```

   