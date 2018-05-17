    $.extend( target , object1  )
    $.extend( [deep ], target, object1 [, objectN ] )

deep	可选。 Boolean类型 指示是否深度合并对象，默认为false。如果该值为true，且多个对象的某个同名属性也都是对象，则该"属性对象"的属性也将进行合并。

```
var marged = $.extend({}, defaults, options); /*合并默认值和选项，不修改默认对象。返回合并后的结果*/ 
```

