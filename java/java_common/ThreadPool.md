参考：

<https://www.cnblogs.com/zhujiabin/p/5404771.html>

<https://www.jianshu.com/p/46728d6bc6b2>

```
线程创建方式

通过实现 Runnable 接口；	实现 run() 方法
通过继承 Thread 类本身；   重写 run() 方法
通过 Callable 和 Future 创建线程。   实现 call() 方法
```



```
线程池
newCachedThreadPool：创建一个可缓存线程池，如果线程池长度超过处理需要，可灵活回收空闲线程，若无可回收，则新建线程。

newFixedThreadPool：创建一个定长线程池，可控制线程最大并发数，超出的线程会在队列中等待

newScheduledThreadPool：创建一个定长线程池，支持定时及周期性任务执行

newSingleThreadExecutor：创建一个单线程化的线程池，它只会用唯一的工作线程来执行任务，保证所有任务按照指定顺序(FIFO, LIFO, 优先级)执行。


```

