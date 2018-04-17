#! /usr/bin/env python
# coding=utf-8

# http://blog.xiayf.cn/2013/01/26/python-string-format/
# https://docs.python.org/3/library/string.html
# 1、使用位置参数
li = ['hoho',18]

print 'my name is {} ,age {}'.format('hoho',18)
print 'my name is {1} ,age {0}'.format(10,'hoho')
print 'my name is {1} ,age {0} {1}'.format(10,'hoho')
print 'my name is {} ,age {}'.format(*li)

# 2、使用关键字参数
hash = {'name':'hoho','age':18}
print 'my name is {name},age is {age}'.format(name='hoho',age=19)
print 'my name is {name},age is {age}'.format(**hash)

# 3、填充与格式化
# :[填充字符][对齐方式 <^>][宽
print '{0:*>10}'.format(10)  ##右对齐        '********10'
print '{0:*<10}'.format(10)  ##左对齐        '10********'
print '{0:*^10}'.format(10)  ##居中对齐       '****10****'

# 4、精度与进制
print '{0:.2f}'.format(1/3)   # '0.33'
print '{0:b}'.format(10)    #二进制 '1010'
print '{0:o}'.format(10)     #八进制 '12'
print '{0:x}'.format(10)     #16进制 'a'
print '{:,}'.format(12369132698)  #千分位格式化 '12,369,132,698'
print  "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
print  "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)  # with 0x, 0o, or 0b as prefix:
print '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
print  '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
print '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
# 5、使用索引
print 'name is {0[0]} age is {0[1]}'.format(li)
print 'name is {0[0]} age is {0[1]}  {1[0]},{1[1]}'.format(li,li)

# object property
# print 'Point({self.x}, {self.y})'.format(self=self)

print  'Correct answers: {:.2%}'.format(1/3.0)

# '{0:{fill}{align}16}'.format(text, fill=align, align=align)
# octets = [192, 168, 0, 1]
# '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
# int(_, 16)

# >>> width = 5
# >>> for num in range(5,12): 
# ...     for base in 'dXob':
# ...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
# ...     print()

#转义大括号
print(" The {} set is often represented as { {0} } ".format("empty")) #  The empty set is often represented as {0}