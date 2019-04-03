```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="sea/sea.js"></script>
    <script type="text/javascript">
        // seajs 的简单配置
        seajs.config({
            //all alias path base on this//所有别名基于本路径
//            base:"../sea-modules/"
            base: "./"

            //define each self path//定义paths，本例未启用
            //,paths:{
            //  "jQueryPath":"jquery"
            //}

            //define each alias name here
            // jQuery: 加载当前目录下的 jquery-1.11.3.min.js
            , alias: { //auto add suffix .js
                "jQuery": "jquery-1.11.3.min"
                , "module1": "./module1"
            }
            , preload: 'jQuery'
            , vars: {
                'locale': 'zh-cn' //本例未启用,在模块中可用格式{key},即{locale}表示变量
            }
        });
        //加载入口模块，加载完成后调用模块的方法
        //        seajs.use(['jQuery','module1'],function($,m){
        //            m.scale();
        //        });
        seajs.use(['jQuery', './module1.js'], function ($, m) {
            m.scale();
            m.scale();
            m.a();
        });
        //seajs.use(['jQuery','../static/hellow/xxxx.js']);
    </script>
</head>
<body>

</body>
</html>
```

```
define(function(require,exports,module){    
    var mode_var=1;
    function scale(){        
        console.log("scale");
        console.log(mode_var);
        mode_var++;     
    }
    function a(){
        console.log("a");
        console.log(mode_var);
        mode_var++;
    }
    exports.scale= scale;
    exports.a= a;
})
```

