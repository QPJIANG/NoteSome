```html
<!--import js-->

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<div id="app">
    {{message}}
</div>
<script>
    var vm = new Vue({
      el:'#app',
      data:{
          message："vue demo"
      }
    });
</script>

```

```html
<!-- 数据属性 -->
<script>
    var data={
        message："vue demo",
        a:1
    }
    var vm = new Vue({
      el:'#app',
      data:data
    });
    //只有当实例被创建时就已经存在于 data 中的属性才是响应式的
    // 新加的属性不会与视图绑定。
    // 使用 Object.freeze()，这会阻止修改现有的属性，也意味着响应系统无法再追踪变化 : Object.freeze(data) 与data绑定的视图在data变化时不会更新。
    
    vm.a == data.a // => true ,一个修改另一个也变化    
</script>
```

```html
<!-- 实例属性 -->
<script>
    var data={
        message："vue demo",
        a:1
    }
    var vm = new Vue({
      el:'#app',
      data:data
    });
  
    vm.$data === data // => true  
    // Vue 实例还暴露了一些有用的实例属性与方法。它们都有前缀 $，以便与用户定义的属性区分开来。
    // https://cn.vuejs.org/v2/api/#%E5%AE%9E%E4%BE%8B%E5%B1%9E%E6%80%A7
</script>

```

```html
<!-- 生命周期 -->
<!-- 不要在选项属性或回调上使用箭头函数 -->
<!-- https://cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E9%92%A9%E5%AD%90 -->
<script>
    var data={
        message："vue demo",
        a:1
    }
    var vm = new Vue({
        el:'#app',        
        data:data,
        beforeCreate:function(){
            // 在实例初始化之后，数据观测（data ovserver）和 event/watcher 事件配置之前被调用。
        },
        created:function(){
            // 实例创建之后被立即调用
            // 在这一步，实例完成：数据观测（data ovserver），属性和方法的运算，event/watcher 事件回调。
            // 此时关在阶段还未开始，$el 属性目前不可见
        },
        beforeMount:function(){
            // 挂载之前被调用，相关的渲染函数首次被调用。
        },
        mounted:function(){
            // el 被新创建的vm.$el 替换，挂载完成。
        },
        beforeUpdate:function(){
        	// 数据更新时调用
    	},
        updated:function(){
            // 组件dom 更新完毕。
        },
        activated:function(){},
        deactivated:function(){},
        beforeDestroy:function(){},
        destroyed:function(){},
        errorCaptured:function(){}
        
        
    });
  
    
</script>

```

