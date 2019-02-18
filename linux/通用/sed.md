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
sed [-hnV][-e]</span></span><span md-inline='reflink'><span class='md-meta md-before'>[</span><a data-ref='文本文件' href='#'><span md-inline='plain'>-f&lt;script文件&gt;</span></a><span class='md-meta md-after'>]</span><span class='md-meta md-before'>[</span><span class='md-content'>文本文件</span><span class='md-meta md-after'>]</span></span></span><span class='md-line md-end-block'  cid = 'n8' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>参数说明：</span></span></p><p  cid = 'n9' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n10' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>-e</span><span md-inline='tag' class='md-tag' spellcheck='false'>&lt;script&gt;</span><span md-inline='plain'>或--expression=</span><span md-inline='tag' class='md-tag' spellcheck='false'>&lt;script&gt;</span><span md-inline='plain'> 以选项中指定的script来处理输入的文本文件。</span></span><span class='md-line md-end-block'  cid = 'n11' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>-f&lt;script文件&gt;或--file=&lt;script文件&gt; 以选项中指定的script文件来处理输入的文本文件。</span></span><span class='md-line md-end-block'  cid = 'n12' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>-h或--help 显示帮助。</span></span><span class='md-line md-end-block'  cid = 'n13' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>-n或--quiet或--silent 仅显示script处理后的结果。</span></span><span class='md-line md-end-block'  cid = 'n14' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>-V或--version 显示版本信息。</span></span><span class='md-line md-end-block'  cid = 'n15' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>动作说明：</span></span></p><p  cid = 'n16' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n17' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>a ：新增， a 的后面可以接字串，而这些字串会在新的一行出现(目前的下一行)～</span></span><span class='md-line md-end-block'  cid = 'n18' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>c ：取代， c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行！</span></span><span class='md-line md-end-block'  cid = 'n19' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>d ：删除，因为是删除啊，所以 d 后面通常不接任何咚咚；</span></span><span class='md-line md-end-block'  cid = 'n20' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>i ：插入， i 的后面可以接字串，而这些字串会在新的一行出现(目前的上一行)；</span></span><span class='md-line md-end-block'  cid = 'n21' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>p ：打印，亦即将某个选择的数据印出。通常 p 会与参数 sed -n 一起运行～</span></span><span class='md-line md-end-block'  cid = 'n22' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>s ：取代，可以直接进行取代的工作哩！通常这个 s 的动作可以搭配正规表示法！例如 1,20s/old/new/g 就是啦</span></span></p><div tabindex='-1' contenteditable='false'  cid = 'n23' mdtype = 'hr' contenteditable='false'  class='md-hr md-end-block' ><hr /></div><p  cid = 'n24' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n25' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>/tmp $ cat testfile </span></span><span class='md-line md-end-block'  cid = 'n26' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>HELLO LINUX!</span><span md-inline='linebreak'>  </span><br/></span><span class='md-line md-end-block'  cid = 'n27' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>Linux is a free unix-type opterating system.</span><span md-inline='linebreak'>  </span><br/></span><span class='md-line md-end-block'  cid = 'n28' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>This is a linux testfile!</span><span md-inline='linebreak'>  </span><br/></span><span class='md-line md-end-block'  cid = 'n29' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>Linux test </span></span><span class='md-line md-end-block'  cid = 'n30' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>/tmp $ sed -e 4a\newline testfile</span></span><span class='md-line md-end-block'  cid = 'n31' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>HELLO LINUX!</span><span md-inline='linebreak'>  </span><br/></span><span class='md-line md-end-block'  cid = 'n32' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>Linux is a free unix-type opterating system.</span><span md-inline='linebreak'>  </span><br/></span><span class='md-line md-end-block'  cid = 'n33' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>This is a linux testfile!</span><span md-inline='linebreak'>  </span><br/></span><span class='md-line md-end-block'  cid = 'n34' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>Linux test </span></span><span class='md-line md-end-block'  cid = 'n35' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>newline</span></span><span class='md-line md-end-block'  cid = 'n36' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>/tmp $ cat testfile </span></span><span class='md-line md-end-block'  cid = 'n37' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>HELLO LINUX!</span><span md-inline='linebreak'>  </span><br/></span><span class='md-line md-end-block'  cid = 'n38' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>Linux is a free unix-type opterating system.</span><span md-inline='linebreak'>  </span><br/></span><span class='md-line md-end-block'  cid = 'n39' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>This is a linux testfile!</span><span md-inline='linebreak'>  </span><br/></span><span class='md-line md-end-block'  cid = 'n40' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>Linux test </span></span></p><h2 cid = 'n42' mdtype = 'heading' contenteditable='true' class='md-end-block md-heading' ><span md-inline='plain'>did not modify the file</span></h2><p  cid = 'n43' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n44' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>nl /etc/passwd | sed &#39;2,5d&#39;   # 将 /etc/passwd 的内容列出并且列印行号，同时，请将第 2~5 行删除！</span></span></p><p  cid = 'n45' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n46' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>nl /etc/passwd | sed &#39;2d&#39;  # 将 /etc/passwd 的内容列出并且列印行号，同时，请将第 2 行删除！</span></span></p><p  cid = 'n47' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n48' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>nl /etc/passwd | sed &#39;3,$d&#39;   #删除第 3 到最后一行</span></span></p><p  cid = 'n49' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n50' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>nl /etc/passwd | sed &#39;2a drink tea&#39;  # 在第二行后(亦即是加在第三行)加上『drink tea?』字样！</span></span></p><p  cid = 'n51' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n52' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>nl /etc/passwd | sed &#39;2i drink tea&#39;  # 在第二行前 加上『drink tea?』字样！</span></span></p><p  cid = 'n53' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n55' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>nl /etc/passwd | sed &#39;2a Drink tea or ......\</span></span></p><blockquote  cid = 'n54' mdtype = 'blockquote'   ><p  cid = 'n56' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n57' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>drink beer ?&#39;			# 第二行后面加入两行字，例如『Drink tea or .....』与『drink beer?』	</span></span></p></blockquote><p  cid = 'n58' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n59' mdtype = 'line' contenteditable='true' ><span md-inline='plain'> nl /etc/passwd | sed &#39;2,5c No 2-5 number&#39; # 将第2-5行的内容取代成为『No 2-5 number』</span></span></p><p  cid = 'n60' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n61' mdtype = 'line' contenteditable='true' ><span md-inline='plain'> nl /etc/passwd | sed -n &#39;5,7p&#39; 	# 仅列出 /etc/passwd 文件内的第 5-7 行</span></span></p><p  cid = 'n62' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n63' mdtype = 'line' contenteditable='true' ><span md-inline='plain'> nl /etc/passwd | sed &#39;/root/p&#39;    # 搜索 /etc/passwd有root关键字的行(如果root找到，除了输出所有行，还会输出匹配行。)</span></span></p><p  cid = 'n64' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n65' mdtype = 'line' contenteditable='true' ><span md-inline='plain'> nl /etc/passwd | sed -n &#39;/root/p&#39;  # 搜索 /etc/passwd有root关键字的行(使用-n的时候将只打印包含模板的行。)</span></span></p><p  cid = 'n66' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n67' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>nl /etc/passwd | sed  &#39;/root/d&#39;  # 删除/etc/passwd所有包含root的行，其他行输出</span></span></p><p  cid = 'n68' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n70' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>nl /etc/passwd | sed -n &#39;/bash/{s/bash/blueshell/;p;q}&#39;  </span><span md-inline='linebreak'>  </span><br/></span></p><h1 cid = 'n69' mdtype = 'heading' contenteditable='true' class='md-end-block md-heading' ><span md-inline='plain'>搜索/etc/passwd,找到root对应的行，执行后面花括号中的一组命令，每个命令之间用分号分隔，这里把bash替换为blueshell，再输出这行：</span></h1><p  cid = 'n71' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n72' mdtype = 'line' contenteditable='true' ></span></p><p  cid = 'n73' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n74' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>sed &#39;s/要被取代的字串/新的字串/g&#39;</span></span><span class='md-line md-end-block'  cid = 'n75' mdtype = 'line' contenteditable='true' ><span md-inline='plain'> /sbin/ifconfig eth0 | grep &#39;inet addr&#39; | sed &#39;s/^.*addr://g&#39;</span></span></p><pre class='md-fences mock-cm md-end-block' lang='' contenteditable='false' cid = 'n76' mdtype = 'fences' contenteditable='false' >	eth0 Link encap:Ethernet HWaddr 00:90:CC:A6:34:84	inet addr:192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0	inet6 addr: fe80::290:ccff:fea6:3484/64 Scope:Link	UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1	.....(以下省略).....	=&gt;	 	inet addr:192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0	=&gt;		192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0</pre><p  cid = 'n77' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n78' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>/sbin/ifconfig eth0 | grep &#39;inet addr&#39; | sed &#39;s/^.</span><span md-inline='em' class=''><span class='md-meta md-before'>*</span><em><span md-inline='plain'>addr://g&#39; | sed &#39;s/Bcast.</span></em><span class='md-meta md-after'>*</span></span><span md-inline='plain'>$//g&#39;</span></span><span class='md-line md-end-block'  cid = 'n79' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>		192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0</span></span><span class='md-line md-end-block'  cid = 'n80' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>	=&gt;</span></span><span class='md-line md-end-block'  cid = 'n81' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>		192.168.1.100</span></span></p><h1 cid = 'n83' mdtype = 'heading' contenteditable='true' class='md-end-block md-heading' ><span md-inline='plain'>一条sed命令，删除/etc/passwd第三行到末尾的数据，并把bash替换为blueshell</span></h1><p  cid = 'n84' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n85' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>nl /etc/passwd | sed -e &#39;3,$d&#39; -e &#39;s/bash/blueshell/&#39;</span></span></p><h1 cid = 'n87' mdtype = 'heading' contenteditable='true' class='md-end-block md-heading' ><span md-inline='plain'>利用 sed 将 regular_express.txt 内每一行结尾若为 . 则换成 !</span></h1><p  cid = 'n88' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n89' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>sed -i &#39;s/</span><span md-inline='escape'><span class='md-meta md-before'>\</span>.</span><span md-inline='plain'>$/</span><span md-inline='escape'><span class='md-meta md-before'>\</span>!</span><span md-inline='plain'>/g&#39; regular_express.txt	(直接修改文件内容(危险动作))</span></span></p><p  cid = 'n90' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n91' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>利用 sed 直接在 regular_express.txt 最后一行加入『# This is a test』</span></span><span class='md-line md-end-block'  cid = 'n92' mdtype = 'line' contenteditable='true' ><span md-inline='plain'>sed -i &#39;$a # This is a test&#39; regular_express.txt</span></span></p><div tabindex='-1' contenteditable='false'  cid = 'n93' mdtype = 'hr' contenteditable='false'  class='md-hr md-end-block' ><hr /></div><p  cid = 'n94' mdtype = 'paragraph'  ><span class='md-line md-end-block'  cid = 'n96' mdtype = 'line' contenteditable='true' ><span md-inline='url' spellcheck='false'><a href='https://www.cnblogs.com/jiangshitong/p/6607552.html'>https://www.cnblogs.com/jiangshitong/p/6607552.html</a>
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
# 搜索/etc/passwd,找到root对应的行，执行后面花括号中的一组命令，每个命令之间用分号分隔，这里把bash替换为blueshell，再输出这行：



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


# 一条sed命令，删除/etc/passwd第三行到末尾的数据，并把bash替换为blueshell
nl /etc/passwd | sed -e '3,$d' -e 's/bash/blueshell/'


# 利用 sed 将 regular_express.txt 内每一行结尾若为 . 则换成 !
sed -i 's/\.$/\!/g' regular_express.txt	(直接修改文件内容(危险动作))

利用 sed 直接在 regular_express.txt 最后一行加入『# This is a test』
sed -i '$a # This is a test' regular_express.txt

----------------------------------------------------------------------------------
https://www.cnblogs.com/jiangshitong/p/6607552.html
https://www.cnblogs.com/-zyj/p/5763303.html
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------

