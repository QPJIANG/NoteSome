常规权限：

```
权限分为三种：读（r=4），写（w=2），执行（x=1）。
可读可执行    （rx=5=4+1）
可读可写      （rw=6=4+2）
可读可写可执行  (rwx=7=4+2+1)。
---------------------------------------------------------------------------
文件权限修改可指定对应的数字来修改，也可使用对应的字母来修改。
---------------------------------------------------------------------------
权限数字：【owner权限】【group权限】【others权限】
chmod 权限数字 文件名
---------------------------------------------------------------------------
chmod u+x 文件名  ： 其owner授予执行权限
chmod go-rw 文件名  ：删除group和others的读和写权限
chmod o=w 文件名  ： others配置写权限

- 表示删除权限
= 表示使之成为唯一的权限
u 代表所有者（user）
g 代表所有者所在的组群（group）
o 代表其他人，但不是u和g （other）
a 代表全部的人，也就是包括u，g和o
r 表示文件可以被读（read）
w 表示文件可以被写（write）
x 表示文件可以被执行
---------------------------------------------------------------------------
chmod 777 文件名 , 等价于 chmod a+wrx 文件名 等价于 chmod a=wrx 文件名
```
![image][tmp]

特殊权限：

```
---------------------------------------------------------------------------
SetUID（简称suid）（数字权限是4000）
4表示其他用户执行文件时，具有与所有者相当的权限
 1.普通用户对可执行的二进制文件，临时拥有二进制文件的属主权限；
 2.如果设置的二进制文件没有执行权限，那么suid的权限显示就是S（大写字母S）； 
 3.特殊权限suid仅对二进制可执行程序有效，其他文件或目录则无效。

$ ll /usr/bin/sudo
-rwsr-xr-x 1 root root 140792 10月 29 17:36 /usr/bin/sudo

chmod u+s  文件名
chmod +s 文件名
chmod -s 文件名

文件夹也可配置s权限。

---------------------------------------------------------------------------
setGID（简称sgid）（数字权限是2000）
chmod g+s  文件名
主要是针对目录进行授权，共享目录。
组权限位上有执行权限，则会在属组主权限位的执行权限上写个s（小写字母）
如果该属组权限位上没有执行权限，则会在属组主权限位的执行权限上写个S


1.针对用户组权限位修改，用户创建的目录或文件所属组和该目录的所属组一致。
2.当某个目录设置了sgid后，在该目录中新建的文件不再是创建该文件的默认所属组 (*)
3.使用sgid可以使得多个用户之间共享一个目录的所有文件变得简单。


chmod a+s  文件名 （suid+sgid）
---------------------------------------------------------------------------
注： o 加s ，ll 没看出权限变化
---------------------------------------------------------------------------
sbit 粘滞位（数字权限是1000）

chmod o+t 目录
	粘滞位，即便是该目录拥有w权限，但是除了root用户，其他用户只能对自己的文件进行删除、移动操作。
	其他用户权限位上有执行权限，则会在其他用户权限位的执行权限上写个t（小写字母）； 如果该其它用户权限位上没有执行权限，则会在其他用户权限位的执行权限上写个T（大写字母）。
	
	普通用户对该目录拥有w和x权限，即普通用户可以在此目录中拥有写入权限，如果没有粘滞位，那么普通用户拥有w权限，就可以删除此目录下的所有文件，包括其他用户建立的文件。
	但是一旦被赋予了粘滞位，除了root可以删除所有文件，普通用户就算有w权限也只能删除自己建立的文件，而不能删除其他用户建立的文件。
---------------------------------------------------------------------------	
chattr：凌驾于r、w、x、suid、sgid之上的权限。

设置特殊权限，chattr命令用来改变文件属性。
    i     #锁定文件，不能编辑，不能修改，不能删除，不能移动，可以执行
    a     #仅可以追加文件，不能编辑，不能删除，不能移动，可以执行
    
    chattr +i 文件  ：防止系文件被修改。
    chattr +a 文件  ：只能往里面追加内容，不能删除
---------------------------------------------------------------------------	    
Linux进程掩码 umask
	登录系统之后，创建一个文件总是有一个默认权限.umask设置了用户创建文件的默认权限。
	系统默认umask为022，那么当我们创建一个目录时，正常情况下目录的权限应该是777，但是umask表示要减去的值，所以新目录文件的权限应该是777-022=755。至于文件的权限也依次类推：666-022=644
	文件：默认权限只能是0,2，4 组合，即只能是0,2,4,6。
	文件666-umask 后的值于权限对应关系： 6->6;5->6;4->4;3->4;2->2;1->2;0->0。 减后值为奇数则+1.
	
	
	文件基数为666，目录为777
	chmod是设哪个位，哪么哪个位就有权限，而umask是设哪个位，则哪个位上就没权限
```























[tmp]:data:image/png;base64,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
