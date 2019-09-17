



```
元注解
@Target：注解的作用目标
@Retention：注解的生命周期
@Documented：注解是否应当被包含在 JavaDoc 文档中
@Inherited：是否允许子类继承该注解

@Repeatable（JDK1.8加入）： 注解可以同时作用一个对象多次，但是每次作用注解又可以代表不同的含义
```

```
@Target
ElementType.TYPE：允许被修饰的注解作用在类、接口和枚举上
ElementType.FIELD：允许作用在属性字段上
ElementType.METHOD：允许作用在方法上
ElementType.PARAMETER：允许作用在方法参数上
ElementType.CONSTRUCTOR：允许作用在构造器上
ElementType.LOCAL_VARIABLE：允许作用在本地局部变量上
ElementType.ANNOTATION_TYPE：允许作用在注解上
ElementType.PACKAGE：允许作用在包上
```

```
@Retention 
RetentionPolicy.SOURCE：当前注解编译期可见，不会写入 class 文件
RetentionPolicy.CLASS：类加载阶段丢弃，会写入 class 文件
RetentionPolicy.RUNTIME：永久保存，可以反射获取
```



```
注解的本质就是一个Annotation接口
```



```
定义：
public @interface MyTestAnnotation {

}
```

```
注解读取： 反射
isAnnotationPresent（注解类.class） :   是否使用指定注解
getAnnotation(注解类.class) : 			获取注解（Annotation），返回值为泛型
									  通过Annotation 可获取注解的数据。


类获取属性
    Field[] getDeclaredFields() 
    public Field getDeclaredField(String name)

获取方法
    Method[]  getDeclaredMethods()
    public Method getDeclaredMethod(String name, Class<?>... parameterTypes)

```



```
使用场景：
	注解用于配置
```

