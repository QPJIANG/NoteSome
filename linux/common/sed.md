# replace

```
sed -i "s#the_string_to_be_replace#the_repalce_string#g" file_to_be_replace
```

```
#!/bin/sh

#
# replace python env
#
cd `dirname $0`
CURRENT_DIR=$(pwd)

REPLACE_FROM='/data/github/django/python3/bin/python3.6'
REPLACE_TO='/soft/python3/bin/python3'
IGNORE_FILE='replace.sh'

grep "$You can't use 'macro parameter character #' in math modeREPLACE_FROM" . -lR|grep -v replace.sh|xargs sed -i "s#$REPLACE_FROM#$REPLACE_TO#g"
```





http://www.runoob.com/linux/linux-comm-sed.html


语法
```
sed [-hnV][-e<script>][-f<script文件>][文本文件]
```
参数说明：

-e<script>或--expression=<script> 以选项中指定的script来处理输入的文本文件。
-f<script文件>或--file=<script文件> 以选项中指定的script文件来处理输入的文本文件。
-h或--help 显示帮助。
-n或--quiet或--silent 仅显示script处理后的结果。
-V或--version 显示版本信息。
动作说明：

a ：新增， a 的后面可以接字串，而这些字串会在新的一行出现(目前的下一行)～
c ：取代， c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行！
d ：删除，因为是删除啊，所以 d 后面通常不接任何咚咚；
i ：插入， i 的后面可以接字串，而这些字串会在新的一行出现(目前的上一行)；
p ：打印，亦即将某个选择的数据印出。通常 p 会与参数 sed -n 一起运行～
s ：取代，可以直接进行取代的工作哩！通常这个 s 的动作可以搭配正规表示法！例如 1,20s/old/new/g 就是啦

----------------------------------------------------------------------------------
/tmp $ cat testfile 
HELLO LINUX!  
Linux is a free unix-type opterating system.  
This is a linux testfile!  
Linux test 
/tmp $ sed -e 4a\newline testfile
HELLO LINUX!  
Linux is a free unix-type opterating system.  
This is a linux testfile!  
Linux test 
newline
/tmp $ cat testfile 
HELLO LINUX!  
Linux is a free unix-type opterating system.  
This is a linux testfile!  
Linux test 

did not modify the file
----------------------------------------------------------------------------------
nl /etc/passwd | sed '2,5d'   # 将 /etc/passwd 的内容列出并且列印行号，同时，请将第 2~5 行删除！

nl /etc/passwd | sed '2d'  # 将 /etc/passwd 的内容列出并且列印行号，同时，请将第 2 行删除！


nl /etc/passwd | sed '3,$d'   #删除第 3 到最后一行


nl /etc/passwd | sed '2a drink tea'  # 在第二行后(亦即是加在第三行)加上『drink tea?』字样！

nl /etc/passwd | sed '2i drink tea'  # 在第二行前 加上『drink tea?』字样！

nl /etc/passwd | sed '2a Drink tea or ......\
> drink beer ?'			# 第二行后面加入两行字，例如『Drink tea or .....』与『drink beer?』	


 nl /etc/passwd | sed '2,5c No 2-5 number' # 将第2-5行的内容取代成为『No 2-5 number』

 nl /etc/passwd | sed -n '5,7p' 	# 仅列出 /etc/passwd 文件内的第 5-7 行

 nl /etc/passwd | sed '/root/p'    # 搜索 /etc/passwd有root关键字的行(如果root找到，除了输出所有行，还会输出匹配行。)

 nl /etc/passwd | sed -n '/root/p'  # 搜索 /etc/passwd有root关键字的行(使用-n的时候将只打印包含模板的行。)

nl /etc/passwd | sed  '/root/d'  # 删除/etc/passwd所有包含root的行，其他行输出

nl /etc/passwd | sed -n '/bash/{s/bash/blueshell/;p;q}'    
### 搜索/etc/passwd,找到root对应的行，执行后面花括号中的一组命令，每个命令之间用分号分隔，这里把bash替换为blueshell，再输出这行：



sed 's/要被取代的字串/新的字串/g'
 /sbin/ifconfig eth0 | grep 'inet addr' | sed 's/^.*addr://g'

		eth0 Link encap:Ethernet HWaddr 00:90:CC:A6:34:84
		inet addr:192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0
		inet6 addr: fe80::290:ccff:fea6:3484/64 Scope:Link
		UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
		.....(以下省略).....
		=>
		 	inet addr:192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0
		=>
			192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0

/sbin/ifconfig eth0 | grep 'inet addr' | sed 's/^.*addr://g' | sed 's/Bcast.*$//g'
		192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0
	=>
		192.168.1.100


###  一条sed命令，删除/etc/passwd第三行到末尾的数据，并把bash替换为blueshell
nl /etc/passwd | sed -e '3,$d' -e 's/bash/blueshell/'


###  利用 sed 将 regular_express.txt 内每一行结尾若为 . 则换成 !
sed -i 's/\.$/\!/g' regular_express.txt	(直接修改文件内容(危险动作))

利用 sed 直接在 regular_express.txt 最后一行加入『# This is a test』
sed -i '$a # This is a test' regular_express.txt

----------------------------------------------------------------------------------
https://www.cnblogs.com/jiangshitong/p/6607552.html
https://www.cnblogs.com/-zyj/p/5763303.html
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
替换一个目录下所有文件中的指定字符串

```
grep old_str . -R|awk '{print $1}'| awk -F ':' '{print $1}'|xargs  sed -i "s/old_str/new_str/g" 
```



----------------------------------------------------------------------------------

