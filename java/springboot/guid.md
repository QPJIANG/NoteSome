@SpringBootApplication

@Controller     返回viewname
@RestController  返回data(eg: string,json)



@JsonIgnore  ： 对象转json 忽略属性
@JsonFormat(...):   对象转json 时 属性format
@JsonInclude(...)  ： 对象转json 时，属性满足一定条件才进入json

@ControllerAdvice
@ExceptionHandler

@EnableScheduling //开启定时任务

@EnableAsync //开启异步调用方法
@Async       // 异步调用方法修饰





-----------------------------------------------------------------------------------------------------------------------------------------------------------

```
------------------------------------------------------------------------------------
@Controller


------------------------------------------------------------------------------------
参考: https://blog.csdn.net/qq_33800083/article/details/80166144
@Scope描述的是Spring容器是如何新建bean实例的

1.Singleton：一个spring容器只有一个bean的容器（spring默认配置）

2.prototype：每次调用新建一个bean

3.request：web项目中，每一个http request新建一个bean实例

4.session：web项目中，给每一个http session新建一个bean实例

5. global-session    该作用域将bean的定义限制为全局HTTP会话。
------------------------------------------------------------------------------------
参考: https://blog.csdn.net/siwuxie095/article/details/79407097?utm_source=copy
@RequestMapping
作用与class:     不是完整的url
作用与method:    完整url由作用与类上的url 与作用于方法上的url 拼接 而成.
			    限制请求方法:@RequestMapping(value="/hello", method=RequestMethod.POST)
			   				method={RequestMethod.GET,RequestMethod.POST}
				限制请求参数:
					params="userId" 请求参数中必须包含 userId
					params="!userId" 请求参数中不能包含 userId
					params="userId!=1" 请求参数中必须包含 userId，但不能为 1
					params={"userId","userName"} 必须包含 userId 和 userName 参数

映射单个URL
@RequestMapping("") 或 @RequestMapping(value="")

映射多个URL
@RequestMapping({"",""}) 或 @RequestMapping(value={"",""})
路径开头是否加斜杠/均可，建议加上，如：@RequestMapping("/hello")

简单映射: "/hello"

匹配映射:? 匹配任何单字符,* 匹配任意数量的字符（含 0 个）,** 匹配任意数量的目录（含 0 个）

占位映射: 通过@PathVariable("") 注解将占位符中的值绑定到方法参数上
@RequestMapping("/user/{userId}/show")
public ModelAndView show(@PathVariable("userId") Long userId) {

----------------------------------------------------------------------------------
参考: https://blog.csdn.net/swebin/article/details/92795422
@RequestParam("") 注解将请求参数绑定到方法参数上

@ReqeustBody:
　　　　常用来处理content-type不是默认的application/x-www-form-urlcoded编码的内容，
　　　  好比：application/json或者是application/xml等，常常用来其来处理application/json类型
注意：@requestBody接收的是前端传过来的json字符串,而不是对象

请求参数:
	简单参数:
        表单中input的name值和Controller的参数变量名保持一致；
        不一致时:可使用 @RequestParam 来指定需要绑定的表单参数
    实体类参数:
    	表单中input的name值 与实体类的属性名一致
    	时间类型等需要做转换
    	复合POJO（实体类）类型的绑定:
    		表单name属性值: 复合属性名.字段名 name="ojbxx.propetyxxx"
    	数组类型: form中 name值相同的输入值构成的集合 
    	
```



