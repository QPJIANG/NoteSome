官网： https://knockoutjs.com/index.html

文档： https://knockoutjs.com/documentation/introduction.html

```
Knockout是一个JavaScript库，可帮助您使用干净的底层数据模型创建丰富，响应迅速的显示和编辑器用户界面。只要您有动态更新的UI部分（例如，根据用户的操作或外部数据源更改而更改），KO可以帮助您更简单，更可维护地实施它。

标题功能：

优雅的依赖关系跟踪 - 在数据模型发生变化时自动更新UI的正确部分。
声明性绑定 - 将UI的各个部分连接到数据模型的简单明了的方法。您可以使用任意嵌套的绑定上下文轻松构建复杂的动态UI。
简单可扩展 - 将自定义行为实现为新的声明性绑定，以便在几行代码中轻松重用。
额外的好处：

纯JavaScript库 - 适用于任何服务器或客户端技术
可以添加到现有Web应用程序之上，而无需进行重大架构更改
紧凑 - gzipping后约13kb
适用于任何主流浏览器（IE 6 +，Firefox 2 +，Chrome，Safari，Edge等）
全面的规范套件（开发BDD风格）意味着它可以在新的浏览器和平台上轻松验证其正确的功能
```

applyBindings:

```
var viewModel = {
	modekey1: ko.observable(true) ,
	modekey2: ko.observable(true) 
};
function viewMode2(){
    this.modekey1=ko.observable(true) ;
    this.modekey2=ko.observable(true) ;
}    
ko.applyBindings(viewModel,document.getElementById("x2"));
ko.applyBindings(viewMode2);

同一个dom 只能bind 一次。
```

observable， subscribe

```
   var x= ko.observable(false);

    //    observable 值变化时调用
    //    subscribe(function(newvalue))
    //    subscribe(function(oldvalue),null,"beforeChange")
    //    参考 https://knockoutjs.com/documentation/observables.html

    var subscription = x.subscribe(function (val) {
        console.log("old value",val);
    },null, "beforeChange");
    x(true)

    subscription.dispose(); // I no longer want notifications
```

