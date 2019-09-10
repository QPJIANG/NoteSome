

 [求shel取最后一次出现的字符串以后的行](http://bbs.chinaunix.net/thread-4158607-1-1.html)

```
不包含关键字行
sed -e :a -e "N;/Performance Statistics/s/.*\n//" -e '$!ba' file

包含关键字行
awk '/Performance/{s=""}{s=s?s"\n"$0:$0}END{print s}' tmp    


```



