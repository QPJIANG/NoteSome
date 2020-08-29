

web.xml

参考：

<https://www.cnblogs.com/hellojava/archive/2012/12/28/2835730.html>

<https://www.cnblogs.com/Jimc/p/9565603.html>

```
WEB容器的加载顺序是：ServletContext -> context-param -> listener -> filter -> servlet。并且这些元素可以配置在文件中的任意位置。
```

```
1. web 启动： WEB容器创建一个ServletContext（servlet上下文），这个web项目的所有部分都将共享这个上下文。
2. 容器将<context-param>转换为键值对，并交给servletContext。
3. 容器创建<listener>中的类实例，创建监听器。  (可读取servletContext 中的内容)
4. 载入filter, 创建过滤链
5. 载入servlet, 映射请求路径
```







spring 启动：

```
1. 创建ServletContext
2. 加载 <context-param> 到 servletContext
3. 创建监听器： 初始化spring ：根据contextConfigLocation配置创建bean,配置数据库等。
4. 载入filter, 创建过滤链
5. 载入servlet, 映射请求路径 （静态动态资源路径映射，配置viewresover）
```



```xml
<servlet></servlet> 在向servlet或JSP页面制定初始化参数或定制URL时，必须首先命名servlet或JSP页面。Servlet元素就是用来完成此项任务的。
<servlet-mapping></servlet-mapping> 服务器一般为servlet提供一个缺省的URL：http://host/webAppPrefix/servlet/ServletName.但是，常常会更改这个URL，以便servlet可以访问初始化参数或更容易地处理相对URL。在更改缺省URL时，使用servlet-mapping元素。 

<session-config></session-config> 如果某个会话在一定时间内未被访问，服务器可以抛弃它以节省内存。 可通过使用HttpSession的setMaxInactiveInterval方法明确设置单个会话对象的超时值，或者可利用session-config元素制定缺省超时值。

<mime-mapping></mime-mapping>如果Web应用具有想到特殊的文件，希望能保证给他们分配特定的MIME类型，则mime-mapping元素提供这种保证。 
    
<welcome-file-list></welcome-file-list> 指示服务器在收到引用一个目录名而不是文件名的URL时，使用哪个文件。 

<error-page></error-page> 在返回特定HTTP状态代码时，或者特定类型的异常被抛出时，能够制定将要显示的页面。 

<taglib></taglib> 对标记库描述符文件（Tag Libraryu Descriptor file）指定别名。此功能使你能够更改TLD文件的位置，而不用编辑使用这些文件的JSP页面。 

<resource-env-ref></resource-env-ref>声明与资源相关的一个管理对象。 
<resource-ref></resource-ref> 声明一个资源工厂使用的外部资源。 
<security-constraint></security-constraint> 制定应该保护的URL。它与login-config元素联合使用 
<login-config></login-config> 指定服务器应该怎样给试图访问受保护页面的用户授权。它与sercurity-constraint元素联合使用。 

<security-role></security-role>给出安全角色的一个列表，这些角色将出现在servlet元素内的security-role-ref元素的role-name子元素中。分别地声明角色可使高级IDE处理安全信息更为容易。 

<env-entry></env-entry>声明Web应用的环境项。 
<ejb-ref></ejb-ref>声明一个EJB的主目录的引用。 
<ejb-local-ref></ejb-local-ref>声明一个EJB的本地主目录的应用。 

Web应用图标
<icon> 
    <small-icon>/images/app_small.gif</small-icon> 
    <large-icon>/images/app_large.gif</large-icon> 
</icon> 
定义了WEB应用的名字 
<display-name>App Name</display-name>

Web 应用描述
<disciption>This is a app disciption.</disciption>

上下文初始化参数
<context-param> 
    <param-name>ContextParameter</para-name> 
    <param-value>test</param-value> 
    <description>It is a test parameter.</description> 
</context-param> 


过滤器
<filter> 
    <filter-name>setCharacterEncoding</filter-name> 
    <filter-class>com.xxx.setCharacterEncodingFilter</filter-class> 
    <init-param> 
        <param-name>encoding</param-name> 
        <param-value>utf-8</param-value> 
    </init-param> 
</filter> 
<filter-mapping> 
    <filter-name>setCharacterEncoding</filter-name> 
    <url-pattern>/*</url-pattern> 
</filter-mapping>

监听器
<listener> 
    <listerner-class>listener.SessionListener</listener-class> 
</listener>

servlets
<servlet> 
    <servlet-name>test</servlet-name> 
    <servlet-class>TestServlet</servlet-class> 
</servlet> 
<servlet-mapping> 
    <servlet-name>test</servlet-name> 
    <url-pattern>/test</url-pattern> 
</servlet-mapping> 

<servlet> 
    <servlet-name>test2</servlet-name> 
    <servlet-class>TestServlet2</servlet-class> 
    <init-param> 
        <param-name>foo</param-name> 
        <param-value>bar</param-value> 
    </init-param> 
    <run-as> 
        <description>Security role for anonymous access</description> 
        <role-name>tomcat</role-name> 
    </run-as> 
    
    <!--   当Web应用启动时，装载Servlet的次序, 当值为正数或零时：Servlet容器先加载数值小的servlet，再依次加载其他数值大的servlet. 当值为负或未定义：Servlet容器将在Web客户首次访问这个servlet时加载它 
                -->
    <load-on-startup>1</load-on-startup>
</servlet> 
<servlet-mapping> 
    <servlet-name>test2</servlet-name> 
    <url-pattern>/test2</url-pattern> 
</servlet-mapping>         


session:
<session-config> 
    <session-timeout>120</session-timeout> 
</session-config> 

MIME类型配置
<mime-mapping> 
    <extension>html</extension> 
    <mime-type>text/html</mime-type> 
</mime-mapping> 

welcome page
<welcome-file-list> 
    <welcome-file>index.jsp</welcome-file> 
    <welcome-file>index.html</welcome-file> 
    <welcome-file>index.htm</welcome-file> 
</welcome-file-list> 

error page 
<error-page> 
    <error-code>404</error-code> 
    <location>/404.jsp</location> 
</error-page> 
<error-page> 
    <exception-type>java.lang.NullException</exception-type> 
    <location>/error.jsp</location> 
</error-page> 


TLD
<jsp-config> 
    <taglib> 
        <taglib-uri>http://jakarta.apache.org/tomcat/debug-taglib</taglib-uri> 
        <taglib-location>/WEB-INF/pager-taglib.tld</taglib-location> 
    </taglib> 
</jsp-config> 

资源工厂配置
<resource-ref> 
    <res-ref-name>mail/Session</res-ref-name> 
    <res-type>javax.mail.Session</res-type> 
    <res-auth>Container</res-auth> 
</resource-ref> 

```

