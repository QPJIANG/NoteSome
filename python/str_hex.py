#! /usr/bin/env python
# coding=utf-8

# hex to string
x = 'e8 ae be e5 88 ab e6 95 85 e9 9a 9c 2c e8 ae be e5 88 ab e6 95 85 e9 9a 9c 2c e8 ae be e5 88 ab e6 95 85 e9 9a 9c 2c e8 ae be e5 88 ab e6 95 85 e9 9a 9c'
z = str(bytearray.fromhex(x))
print z

# string to hex
s=  "设别故障,设别故障,设别故障,设别故障"
print " ".join("{:02X}".format(ord(c)) for c in s)

# string to hex
x=' '.join(x.encode('hex') for x in 'Hello World!')
print x
print  str(bytearray.fromhex(x))