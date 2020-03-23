```
参考： https://blog.csdn.net/bdqx_007/article/details/94836637
```

1. 匿名参数

   ```
   mapper： 普通函数
   
   xml:   #{参数名}  ,不需要 parameterType
   ```

   

2. @Param注解

   ```
   mapper： 普通函数
   
   xml:   #{参数名（@Param 设置的名称）}  ,不需要 parameterType
   ```

   

3. map

   ```
   mapper： 函数参数为map 类型
   xml: 设置parameterType="map"   #{key (map 键)} 
   ```

   

4. bean

   ```
   mapper： 函数参数为 bean 类型
   xml: 设置parameterType="xxx.xx.bean"  #{key(bean 属性名)} 
   ```

   

5. json

   ```
   mapper: 与map,bean 使用方式类似
   xml: 设置parameterType="xxx.xx.bean"  #{key(json 键)} 
   ```

   

6. list,set,array

   ```
   mapper: 使用方式与匿名参数类似
   xml:不需要 parameterType, 
   list mapper参数名
    <foreach collection="list" open="(" separator="," close=")" item="xxx">
         #{xxx}s
       </foreach>
   ```

   

7. 参数类型为对象+集合 (对象属性为集合)

   ```
   mapper: 与bean,map 类型类似
   xml: 设置parameterType="xxx.xx.bean"
   #{变量名.属性名}
   ```



1-6： parameterType： 可直接使用#{属性名}获取传值