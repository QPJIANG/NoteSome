#coding=utf-8

import uuid

name = 'test_name'
namespace = 'test_namespace'

print uuid.uuid1()
print uuid.uuid3(namespace,name)
print uuid.uuid4()
print uuid.uuid5(namespace,name)

'''
python中的uuid模块基于信息如MAC地址、时间戳、命名空间、随机数、伪随机数来uuid。具体方法有如下几个：　　

　　uuid.uuid1()　　基于MAC地址，时间戳，随机数来生成唯一的uuid，可以保证全球范围内的唯一性。

　　uuid.uuid2()　　算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。不过需要注意的是python中没有基于DCE的算法，所以python的uuid模块中没有uuid2这个方法。

　　uuid.uuid3(namespace,name)　　通过计算一个命名空间和名字的md5散列值来给出一个uuid，所以可以保证命名空间中的不同名字具有不同的uuid，但是相同的名字就是相同的uuid了

　　uuid.uuid4()　　通过伪随机数得到uuid，是有一定概率重复的

　　uuid.uuid5(namespace,name)　　和uuid3基本相同，只不过采用的散列算法是sha1

'''