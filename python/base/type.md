```
from types import MethodType

def set_age(self,age):
    self.age=age
class Stu(object):
    pass
Stu.set_age=MethodType(set_age,Stu)
```

​	