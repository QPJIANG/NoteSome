参考:<https://www.cnblogs.com/avivaye/p/5341341.html>



### Maven本质上是一个插件框架，它的核心并不执行任何具体的构建任务，所有这些任务都交给插件来完成。

编译源代码是由maven-compiler-plugin完成的

每个任务对应了一个插件目标（goal），每个插件会有一个或者多个目标.





### 用户可以通过两种方式调用Maven插件目标。

第一种方式是将插件目标与生命周期阶段（lifecycle phase）绑定，这样用户在命令行只是输入生命周期阶段而已。

例如Maven默认将maven-compiler-plugin的compile目标与compile生命周期阶段绑定，因此命令mvn compile实际上是先定位到compile这一生命周期阶段，然后再根据绑定关系调用maven-compiler-plugin的compile目标。

第二种方式是直接在命令行指定要执行的插件目标。

例如mvn archetype:generate 就表示调用maven-archetype-plugin的generate目标，这种带冒号的调用方式与生命周期无关。





### Maven官方有两个插件列表：

第一个列表的GroupId为org.apache.maven.plugins，这里的插件最为成熟，具体地址为：<http://maven.apache.org/plugins/index.html>。

第二个列表的GroupId为org.codehaus.mojo，这里的插件没有那么核心，但也有不少十分有用，其地址为：<http://mojo.codehaus.org/plugins.html>。