### 自定义command

```
pip install flask_script
```

基本用法参考： <https://www.cnblogs.com/buyisan/p/8270283.html>

```
#-*-coding:utf8-*-  

from flask_script import Manager,Command,Server  
from app import app  
  
manager = Manager(app) 
# 方式1
class Hello(Command):  
    'hello world 1'  
    def run(self):  
        print('hello world')

manager.add_command('hello', Hello()) 

# 方式2
@manager.command  
def hello2():  
    'hello world 2 '  
    print('hello world')

# 方式3
@manager.option('-n', '--name', dest='name', help='Your name', default='world')    #命令既可以用-n,也可以用--name，dest="name"用户输入的命令的名字作为参数传给了函数中的name
@manager.option('-u', '--url', dest='url', default='www.csdn.com')  #命令既可以用-u,也可以用--url,dest="url"用户输入的命令的url作为参数传给了函数中的url
def hello3(name, url):  
    'hello world or hello <setting name>'  
    print('hello3', name)  
    print(url)  



manager.add_command("runserver2", Server()) #命令是runserver




if __name__ == '__main__':  
    manager.run()
```

