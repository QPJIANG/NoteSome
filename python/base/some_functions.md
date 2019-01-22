zip:

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

