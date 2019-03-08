```
import os
import sys
print(os.path.abspath(__file__))
print(os.path.realpath(__file__))


x.py 源文件， xx.py 为软链接，xxx.py 硬链接
x.py
xx.py -> x.py
xxx.py

执行软链接，输出:
/tmp/xx.py
/tmp/x.py

执行硬链接输出：
/tmp/xxx.py
/tmp/xxx.py

```

