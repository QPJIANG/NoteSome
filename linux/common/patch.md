补丁：

通过diff 生成补丁文件，通过patch 打补丁

```
diff -ur 
diff -u

patch -R 
patch 
```

example:

```
$ tree
.
├── v1
│   └── a
└── v2
    └── a


$ diff -ur v1 v2 > patch
```

```
p0

补丁：
$ patch -p0 <patch 
patching file v1/a

恢复：
$ patch -R -p0 <patch 
patching file v1/a
```

```
p1
补丁：
v1 $ patch -p1 <../patch 
patching file a
恢复：
v1 $ patch -R -p1 <../patch 
patching file a

```

```
$ cat patch 
diff -ur v1/a v2/a

-p 剥离层级
patch 执行路径与patch 中的文件的层级关系。
在v1,v2 同级时执行patch: v1/a v2/a  剥离层级0,  留下 v1/a v2/a ： 当前路径开始找 ./v1/a ./v2/2
在v1,v2 目录下执行patch：需剥离 v1,v2 剥离层级1,  留下 a a  ： 当前路径开始找 ./a  ./a

及 ./ 开始 。 patch diff 路径截取多少层目录后是匹配的。

```

