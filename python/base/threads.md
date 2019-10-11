参考：

<https://www.runoob.com/python/python-multithreading.html>

<https://docs.python.org/zh-cn/3.7/library/threading.html

```
方法1：
thread.start_new_thread ( function, args[, kwargs] )

方法二：
类继承 threading.Thread ，并重写 run 函数 

threading.Thread(target=xxx,ars[,...]).start

########################################################################################
线程锁：
class threading.Lock ：锁
class threading.RLock： 重入锁 ，重入锁必须由获取它的线程释放。一旦线程获得了重入锁，同一个线程再次获取它将不阻塞；线程必须在每次获取它时释放一次。


threadLock = threading.Lock()
 # 获得锁，成功获得锁定后返回True
 # 可选的timeout参数不填时将一直阻塞直到获得锁定
 # 否则超时后将返回False
 threadLock.acquire()
 
 # you code here
 
 # 释放锁
 threadLock.release()
######################################################################################## 
with some_lock:
    # do something...
相当于:
some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()	
########################################################################################
 
 
 
队列： Queue
Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。

########################################################################################
```

