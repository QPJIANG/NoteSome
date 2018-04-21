```python
# -*- coding: utf-8 -*-
import os
import threading
import multiprocessing
import time


def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:', pipe.recv())


def proc2(pipe):
    print('proc2 rec:', pipe.recv())
    pipe.send('hello, too')

def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    time.sleep(1)
    print("sleep end")
    lock.release()
    pass

def worker2(i,lock):
    lock.acquire()
    print('Worker',os.getpid())
    print(i)
    time.sleep(1)
    print("sleep end")
    lock.release()
    pass

def testpip():
    import multiprocessing as mul

    # Build a pipe
    pipe = mul.Pipe()

    # Pass an end of the pipe to process 1
    p1 = mul.Process(target=proc1, args=(pipe[0],))
    # Pass the other end of the pipe to process 2
    p2 = mul.Process(target=proc2, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

def testthread():
    print('Main:', os.getpid())
    record = []
    lock = threading.Lock()
    for i in range(5):
        thread = threading.Thread(target=worker, args=('thread', lock))
        thread.start()
        record.append(thread)

    for thread in record:
        thread.join()

def testprocess():
    print('Main:', os.getpid())
    jobs = []
    lock = multiprocessing.Lock()
    for i in range(5):
        p = multiprocessing.Process(target=worker2, args=("process", lock))
        jobs.append(p)
        p.start()
    pass

    for pro in jobs:
        pro.join()

# input worker
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put(info)

# output worker
def outputQ(queue,lock):
    info = queue.get()
    lock.acquire()
    print (str(os.getpid()) + '(get):' + info)
    lock.release()

def testqueue():
    record1 = []  # store input processes
    record2 = []  # store output processes
    lock = multiprocessing.Lock()  # To prevent messy print
    queue = multiprocessing.Queue(3)

    # input processes
    for i in range(10):
        process = multiprocessing.Process(target=inputQ, args=(queue,))
        process.start()
        record1.append(process)

    # output processes
    for i in range(10):
        process = multiprocessing.Process(target=outputQ, args=(queue, lock))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    queue.close()  # No more object will come, close the queue

    for p in record2:
        p.join()



if __name__ == '__main__':
    # testthread()
    # testprocess()
    # testpip()
    testqueue()

```

```python
import queue

from multiprocessing.managers import BaseManager

class Job:
    def __init__(self, job_id):
        self.job_id = job_id


class Master:
    def __init__(self):
        # 派发出去的作业队列
        self.dispatched_job_queue = queue()
        # 完成的作业队列
        self.finished_job_queue = queue()
    def get_dispatched_job_queue(self):
        return self.dispatched_job_queue
    def get_finished_job_queue(self):
        return self.finished_job_queue
    def start(self):
        # 把派发作业队列和完成作业队列注册到网络上
        BaseManager.register('get_dispatched_job_queue', callable=self.get_dispatched_job_queue)
        BaseManager.register('get_finished_job_queue', callable=self.get_finished_job_queue)
        # 监听端口和启动服务
        manager = BaseManager(address=('0.0.0.0', 8888), authkey='jobs')
        manager.start()
        # 使用上面注册的方法获取队列
        dispatched_jobs = manager.get_dispatched_job_queue()
        finished_jobs = manager.get_finished_job_queue()
        # 这里一次派发10个作业，等到10个作业都运行完后，继续再派发10个作业
        job_id = 0
        while True:
            for i in range(0, 10):
                job_id = job_id + 1
                job = Job(job_id)
                print('Dispatch job: %s' % job.job_id)
                dispatched_jobs.put(job)
        while not dispatched_jobs.empty():
            job = finished_jobs.get(60)
        print('Finished Job: %s' % job.job_id)
        manager.shutdown()

if __name__ == '__main__':
    master = Master()
    master.start()
    pass
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

def test():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    # QueueManager.register('get_task_queue', callable=lambda: task_queue)
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    freeze_support()
    test()


# # -*- coding: utf-8 -*-
#
# import random, time, queue,pickle
# from multiprocessing.managers import BaseManager
#
# # 发送任务的队列:
# task_queue = queue.Queue()
# # 接收结果的队列:
# result_queue = queue.Queue()
#
# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
# # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
# # 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# # 启动Queue:
# #manager.start()
# s = manager.get_server()
# s.serve_forever()
#
# # 获得通过网络访问的Queue对象:
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# print('master exit.')
#
#
#

```

```
# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
try:
    m.connect()
except:
    print("连接主机失败")
    exit()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(13):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(4)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
    except:
        print("其他异常退出")
        exit()
# 处理结束:
print('worker exit.')
```

