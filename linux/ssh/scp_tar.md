把home文件打包并解压到/datavg35下
```
  tar -cvf- home |(cd /datavg35; tar -xvf -)
```
 把A机的t11.txt 打包并传送到B机上
 ```
  tar cvfz - t11.txt|ssh erpprd "cat >t11.tar.gz"

 ```
把A机的t11.txt 打包并传送到B机上的/tmp目录下
```
tar cvfz - t11.txt |ssh erpprd "cd /tmp;cat >t11.tar.gz"

```
将A机的t11.txt压缩文件，复制到B机并解压缩
```
zcat dir.tar | ssh 192.168.0.116 "cd /opt; tar -xf -"

```
在A机上一边打包t11.txt文件，一边传输到B机并解压
```
 tar cvfz - t11.txt |ssh erpprd "cd /tmp; tar -xvfz -"


 传输到远程：tar czf - file| ssh server "tar zxf -"

 压缩到远程：tar czf - file| ssh server "cat > file.tar.gz"

 解压到远程：ssh server "tar zxf -" < file.tar.gz

 解压到本地：ssh server "cat file.tar.gz" | tar zxf -
```
