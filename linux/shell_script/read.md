1、基本读取

```
!/bin/bash
echo -n "Enter your name:"   //参数-n的作用是不换行，echo默认是换行
read  name                   //从键盘输入
echo "hello $name"           //显示信息
exit 0                      

#!/bin/bash
read -p "Enter your name:" name
echo "hello $name"
exit 0
```

2、计时输入.

```
#!/bin/bash
if read -t 5 -p "please enter your name:" name
then
    echo "hello $name ,welcome to my script"
else
    echo "sorry,too slow"
fi
exit 0

# -t选项指定read命令等待输入的秒数。当计时满时，read命令返回一个非零退出状态;
```

```
#!/bin/bash
read -n1 -p "Do you want to continue [Y/N]?" answer
case $answer in
Y | y)
      echo "fine ,continue";;
N | n)
      echo "ok,good bye";;
*)
     echo "error choice";;
esac
exit 0
# -n选项，后接数值1，指示read命令只要接受到一个字符就退出。只要按下一个字符进行回答，read命令立即
# 接受输入并将其传给变量。无需按回车键。
```

3、默读（输入不显示在监视器上）

```
#!/bin/bash
read  -s  -p "Enter your password:" pass
echo "your password is $pass"
exit 0
# -s选项能够使read命令中输入的数据不显示在监视器上（实际上，数据是显示的，只是read命令将文本颜色设置成
# 与背景相同的颜色）。
```

4、读文件

```
#!/bin/bash
count=1    						
cat test | while read line        //cat 命令的输出作为read命令的输入,read读到的值放在line中
do
   echo "Line $count:$line"
   count=$[ $count + 1 ]          //注意中括号中的空格。
done
echo "finish"
exit 0
```

