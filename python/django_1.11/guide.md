```
django-admin.py startproject project_name

cd project_name

可用命令
python manage.py 


python manage.py startapp app_name

# 1. 创建更改的文件
python manage.py makemigrations
# 2. 将生成的py文件应用到数据库
python manage.py migrate


python manage.py runserver
python manage.py runserver 8001
python manage.py runserver 0.0.0.0:8000


清空数据库
python manage.py flush
此命令会询问是 yes 还是 no, 选择 yes 会把数据全部清空掉，只留下空表。



python manage.py createsuperuser
# 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填

# 修改 用户密码可以用：
python manage.py changepassword username


导出数据 导入数据
python manage.py dumpdata
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json


python manage.py shell



模型：
models.py
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

同步数据库：
python manage.py makemigrations
python manage.py migrate    

测试数据：
$ python manage.py shell 
>>> from app_name.models import Person
>>> Person.objects.create(name="test", age=24)
<Person: Person object>
>>> Person.objects.get(name="test")
<Person: Person object>
>>>


Person.objects.create(name=name,age=age)
p = Person(name="WZ", age=23)
p.save()

p = Person(name="TWZ")
p.age = 23
p.save()
Person.objects.get_or_create(name="WZT", age=23)
这种方法是防止重复很好的方法，但是速度要相对慢些，返回一个元组，第一个为Person对象，第二个为True或False, 新建时返回的是True, 已经存在时返回False.



Person.objects.all()
Person.objects.get(name=name)

get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
Person.objects.filter(name="abc")  # 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人
Person.objects.filter(name__iexact="abc")  # 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件
Person.objects.filter(name__contains="abc")  # 名称中包含 "abc"的人
Person.objects.filter(name__icontains="abc")  #名称中包含 "abc"，且abc不区分大小写
Person.objects.filter(name__regex="^abc")  # 正则表达式查询
Person.objects.filter(name__iregex="^abc")  # 正则表达式不区分大小写
filter是找出满足条件的，当然也有排除符合某条件的
Person.objects.exclude(name__contains="te")  # 排除包含 WZ 的Person对象
Person.objects.filter(name__contains="abc").exclude(age=23)  # 找出名称含有abc, 但是排除年龄是23岁的
Person.objects.filter(name__contains="abc").delete() # 删除 名称中包含 "abc"的人
Person.objects.filter(name__contains="abc").update(name='xxx') # 名称中包含 "abc"的人 都改成 xxx
Person.objects.all().delete() # 删除所有 Person 记录
Person.objects.all()[:10] 切片操作，前10条
Person.objects.all()[-10:] 会报错！！！
 
# 1. 使用 reverse() 解决
Person.objects.all().reverse()[:2] # 最后两条
Person.objects.all().reverse()[0] # 最后一条
 
# 2. 使用 order_by，在栏目名（column name）前加一个负号
Author.objects.order_by('-id')[:20] # id最大的20条



qs1 = Pathway.objects.filter(label__name='x')
qs2 = Pathway.objects.filter(reaction__name='A + B >> C')
qs3 = Pathway.objects.filter(inputer__name='WeizhongTu') 
# 合并到一起
qs = qs1 | qs2 | qs3
这个时候就有可能出现重复的 
# 去重方法
qs = qs.distinct()


```

