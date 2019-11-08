参考: <https://blog.csdn.net/qq_26775359/article/details/78266079>

```
ko.utils.arrayForEach(array, callback)

var arr = [1, 2, 3, 4];
ko.utils.arrayForEach(arr, function(el, index) {
    
});

ko.utils.arrayForEach = function (array, action) {
    for (var i = 0, j = array.length; i < j; i++)
        action(array[i], i);
}

```

```
var arr = [1, 2, 3, 4];
var newArr = ko.utils.arrayMap(arr, function(el, index) {
    return el + 1;
});


ko.utils.arrayMap = function (array, mapping) {
    array = array || [];
    var result = [];
    for (var i = 0, j = array.length; i < j; i++)
        result.push(mapping(array[i], i));
    return result;
}


```

```
var arr = [1, 2, 3, 4];
var newArr = ko.utils.arrayFilter(arr, function(el, index) {
    return el > 2;
});

ko.utils.arrayFilter = function (array, predicate) {
    array = array || [];
    var result = [];
    for (var i = 0, j = array.length; i < j; i++)
        if (predicate(array[i], i))
            result.push(array[i]);
    return result;
}
```

```
var arr = [1, 2, 3, 4];
var index = ko.utils.arrayIndexOf(arr, 2);

ko.utils.arrayIndexOf = function (array, item) {
    if (typeof Array.prototype.indexOf == "function")
        return Array.prototype.indexOf.call(array, item);
    for (var i = 0, j = array.length; i < j; i++)
        if (array[i] === item)
            return i;
    return -1;
}
```

```
var arr = [1, 2, 3, 4, 2];
ko.utils.arrayRemoveItem(arr, 2);

ko.utils.arrayRemoveItem = function (array, itemToRemove) {
    var index = ko.utils.arrayIndexOf(array, itemToRemove);
    if (index > 0) {
        array.splice(index, 1);
    }
    else if (index === 0) {
        array.shift();
    }
}
```



```
var arr = [1, 2, 3, 4, 2, 4, '1'];
var newArr = ko.utils.arrayGetDistinctValues(arr);
// [1, 2, 3, 4, '1']

ko.utils.arrayGetDistinctValues = function (array) {
    array = array || [];
    var result = [];
    for (var i = 0, j = array.length; i < j; i++) {
        if (ko.utils.arrayIndexOf(result, array[i]) < 0)
            result.push(array[i]);
    }
    return result;
}

```

```
var arr = [
    {name: "apple"},
    {name: "banana"},
    {name: "cherries"}
];
var item = ko.utils.arrayFirst(arr, function(el, index){
    return el.name === "banana";
})

ko.utils.arrayFirst = function (array, predicate, predicateOwner) {
    for (var i = 0, j = array.length; i < j; i++)
        if (predicate.call(predicateOwner, array[i], i))
            return array[i];
    return null;
}


```

```
var arr = [1, 2, 3];
ko.utils.arrayPushAll(arr, [4, 5]);


ko.utils.arrayPushAll = function (array, valuesToPush) {
    if (valuesToPush instanceof Array)
        array.push.apply(array, valuesToPush);
    else
        for (var i = 0, j = valuesToPush.length; i < j; i++)
            array.push(valuesToPush[i]);
    return array;
}

```

```
ko.utils.addOrRemoveItem(array, value, included)
included为true，则array中含有value不处理，没有则添加； included为false，则array中含有value删除，没有则不处理。

addOrRemoveItem: function(array, value, included) {
    var existingEntryIndex = ko.utils.arrayIndexOf(ko.utils.peekObservable(array), value);
    if (existingEntryIndex < 0) {
        if (included)
            array.push(value);
    } else {
        if (!included)
            array.splice(existingEntryIndex, 1);
    }
}

```

