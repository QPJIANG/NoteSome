python 源码编译为pyc



```
单个文件编译
python -m py_compile myApp.py
python -m py_compile /path/to/{myApp1,myApp2,,...,}.py
 
 
整体批量编译
python -m compileall myProjectDir
```

```
进入shell交互式环境编译
 
import py_compile
py_compile.compile('path/to/myApp.py')
```

```
项目文件整体进行编译
 
import compileall
compileall.compile_dir(dir='path/to/myProjectDir/',force=True)
```

