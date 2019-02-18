zip():
```
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
zip([iterable, ...])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # zip()  参数为多个数组
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [4, 5, 6, 7, 8]
    zipped = zip(a, b)  # 打包为元组的列表
    print zipped
    # [(1, 4), (2, 5), (3, 6)]

    zipped2 = zip(a, c)  # 元素个数与最短的列表一致
    print zipped2
    # [(1, 4), (2, 5), (3, 6)]

    print zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
    # [(1, 2, 3), (4, 5, 6)]

    print zip(zipped)
    # [((1, 4),), ((2, 5),), ((3, 6),)]

    print zip(zipped, [11, 22, 33])
    #[((1, 4), 11), ((2, 5), 22), ((3, 6), 33)]
    pass


```

namedtuple: (元组的升级版本 -- namedtuple(具名元组))
```
import collections

# 两种方法来给 namedtuple 定义方法名
#User = collections.namedtuple('User', ['name', 'age', 'id'])
User = collections.namedtuple('User', 'name age id')
user = User('tester', '22', '464643123') # *var_array  数组依次填值

print(user)
# output:
# User(name='tester', age='22', id='464643123')

data=['tester', '22', '464643123']
user = User(*data)

```

sum: (数组求和)
```
二维数组求和：
[sum(x) for x in var_array] # 得到数组[sum1,sum2,....]
```

map():
Python 2.x 返回列表。
Python 3.x 返回迭代器。
```

>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]

将多个列表相同位置的元素归并到一个元组(与zip 类似)
# python2
>>> print map(None, [2,4,6],[3,2,1])  # 但是在 python3中，返回是一个迭代器，所以它其实是不可调用的
# [(2, 3), (4, 2), (6, 1)]
# python2
print(list(map(None, [2,4,6],[3,2,1])))
```



zip，实现把两个list组合成一个dict

格式为： dict(zip(keys,vals))