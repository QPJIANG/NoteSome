class Test(object):
    def instancefun(self):   #实例方法
        print("instancefun")
        print(self)
    @classmethod
    def classfun(cls):  # 类方法
        print("class fun")
        print(cls)
    @staticmethod
    def staticfun():    # 静态方法
        print("staticfun")


    # other 方法    
    def function():
        print("func")

t=Test()

# 实例对象调用实例方法
print t.instancefun
t.instancefun()

# 类调用类方法
Test.classfun()

# t.function()    # 不能调用

Test.function()     # 可以调用，类似static method

Test.staticfun()    # 类调用静态方法
t.staticfun()       #实例调用静态方法

t.classfun()    #实例调用类方法


Test.instancefun(t)         # 类调用实例方法，带实例参数
Test.instancefun(Test)       # 类调用实例方法，带类参数


'''
    类方法需要@ classmethod 修饰并且有个隐藏参数 cls,
    实例方法必须有个参数 self,
    静态方法必须有 @staticmethod修饰,
    类和实例都可以访问静态方法,
    实例可以访问实例方法也可以访问类方法,
    类可以访问类方法也可以访问实例方法,访问实例方法必须要带参数 self, 可以理解为类其实也是一个实例,类访问实例方法不带参数会报错的.
    类本身可以访问函数,实例却不行.

'''

'''
###################×分×割×线×######################################################

'''
# 实例方法、类方法、静态方法

class MyClass(object):
    
    class_name = "MyClass"  # 类属性, 三种方法都能调用

    def __init__(self):
        self.instance_name = "instance_name"  # 实例属性, 只能被实例方法调用
        self.class_name = "instance_class_name"

    def get_class_name_instancemethod(self):  # 实例方法, 只能通过实例调用
        # 实例方法可以访问类属性、实例属性
        return MyClass.class_name

    @classmethod
    def get_class_name_classmethod(cls):  # 类方法, 可通过类名.方法名直接调用
        # 类方法可以访问类属性，不能访问实例属性
        return cls.class_name

    @staticmethod
    def get_class_name_staticmethod():  # 静态方法, 可通过类名.方法名直接调用
        # 静态方法可以访问类属性，不能访问实例属性
        return MyClass.class_name

    def instance_visit_class_attribute(self):
        # 实例属性与类属性重名时，self.class_name优先访问实例属性
        print "实例属性与类属性重名时，优先访问实例属性"
        print "self.class_name:", self.class_name
        print "MyClass.name:", MyClass.class_name

if __name__ == "__main__":
    MyClass.class_name = "MyClassNew"
    intance_class = MyClass()
    print "instance method:", intance_class.get_class_name_instancemethod()
    print "class method:", MyClass.get_class_name_classmethod()
    print "static method:", MyClass.get_class_name_staticmethod()
    intance_class.instance_visit_class_attribute()

'''
    result:

    instance method: MyClassNew
    class method: MyClassNew
    static method: MyClassNew
    实例属性与类属性重名时，优先访问实例属性
    self.class_name: instance_class_name
    MyClass.name: MyClassNew
'''