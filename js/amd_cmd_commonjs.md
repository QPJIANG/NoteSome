```
参考 ： https://juejin.im/post/59eafd2051882578c6738f69

模块开发
```



```
(function (root, factory) {
        if (typeof define === 'function' && define.amd) {
            // AMD
            define(['jquery'], factory);
        } else if (typeof exports === 'object') {
            // CommonJS
            module.exports = factory(require('jquery'));
        } else {
            //  全局变量
            root.returnExports = factory(root.jQuery);
        }
    }(this, function ($) {
        //    methods
        function myFunc(){};
        //    exposed public method
        return myFunc;
    }));


```

