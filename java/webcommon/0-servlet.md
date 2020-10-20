

参考： <https://www.cnblogs.com/whgk/p/6399262.html>



Servlet 接口

```
/*
 * 1.实例化（使用构造方法创建对象）
 * 2.初始化  执行init方法:
 public void init(ServletConfig arg0) throws ServletException
 * 3.服务    执行service方法 : 
 public void service(ServletRequest arg0, ServletResponse arg1)
 * 4.销毁    执行destroy方法:
 public void destroy() 
 */
 
 使用： 实现接口
```

GenericServlet 类 （是一个抽象类，实现了 Servlet 接口，并且对其中的 init() 和 destroy() 和 service() 提供了默认实现）

```

public void service(ServletRequest arg0, ServletResponse arg1)

 使用： 重写方法
```

HttpServlet 类 （也是一个抽象类，它进一步继承并封装了 GenericServlet，使得使用更加简单方便，由于是扩展了 Http 的内容，所以还需要使用 HttpServletRequest 和 HttpServletResponse，这两个类分别是 ServletRequest 和 ServletResponse 的子类）

```
protected void doGet(HttpServletRequest req, HttpServletResponse resp)
protected void doPost(HttpServletRequest req, HttpServletResponse resp)
。。。。

 使用： 重写方法
```





ServletConfig、ServletContext，request、response

```
ServletConfig：
	获取途径：getServletConfig(); 
	功能：
		getServletName();  //获取servlet的名称，在web.xml中配置的servlet-name
　　　　　　getServletContext(); //获取ServletContext对象
　　　　　　getInitParameter(String); //获取在servlet中初始化参数的值。这里注意与全局初始化参数的区分。这个获取的只是在该servlet下的初始化参数
　　　　　　getInitParameterNames(); //获取在Servlet中所有初始化参数的名字，也就是key值，可以通过key值，来找到各个初始化参数的value值。返回的是枚举类型
```

```
ServletContext对象
	获取途径：getServletContext(); 、getServletConfig().getServletContext();　
	功能：tomcat为每个web项目都创建一个ServletContext实例，tomcat在启动时创建，服务器关闭时销毁，在一个web项目中共享数据，管理web项目资源，为整个web配置公共信息等，通俗点讲，就是一个web项目，就存在一个ServletContext实例，每个Servlet读可以访问到它。
	setAttribute(String name, Object obj) 在web项目范围内存放内容，以便让在web项目中所有的servlet读能访问到
	getAttribute(String name) 通过指定名称获得内容
	removeAttribute(String name) 通过指定名称移除内容  
	
	getInitPatameter(String name)　　//通过指定名称获取初始化值  <context-param>下<param-name> <param-value>配置的参数
	getInitParameterNames()　　//获得枚举类型
	getRealPath(string file_path)  // 获取资源文件全路径 ： getRealPath("/WEB-INF/web.xml")
	获取web项目下指定资源的内容，返回的是字节输入流。InputStream getResourceAsStream(java.lang.String path)
	getResourcePaths(java.lang.String path)  指定路径下的所有内容 getResourcePaths("/WEB-INF")
```



request、response

```
请求与响应：
request:
	应用名称
	url
	资源路径
	协议版本
	协议
	服务器机器域名或ip
	客户端ip
	服务器端口	
	请求头
	参数
	。。。。
	
	请求转发:request.getRequestDispatcher(String path).forward(request,response);　　//path:转发后跳转的页面
	
response:
	响应头： 
	状态
	响应体
	
	response.sendRedirect(string path) : 重定向
	
```

```
contextpath, servletpath, requesturi, realpath

http://localhost:8080/news/main/list.jsp
则执行下面向行代码后打印出如下结果：

1、 System.out.println(request.getContextPath());
打印结果：/news

2、System.out.println(request.getServletPath());
打印结果：/main/list.jsp

3、 System.out.println(request.getRequestURI());
打印结果：/news/main/list.jsp

4、 System.out.println(request.getRealPath("/"));
打印结果： 。。。。。。\webapps\news\test

```

servlet 生命周期：

```
1.被创建：执行init方法，只执行一次： 第一次被访问时，Servlet被创建
2.提供服务：执行service方法，执行多次
3.被销毁：当Servlet服务器正常关闭时，执行destroy方法，只执行一次
```

