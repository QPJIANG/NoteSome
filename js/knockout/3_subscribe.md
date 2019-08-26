```js
ViewModel.testattr.subscribe(function(newValue) {
	alert("The value is " + newValue);
});


var subscription = ViewModel.testattr.subscribe(function(newValue) {
    // 此次使用this, 拿不到ViewModel
 	/* do stuff */
 });
// ...then later...
subscription.dispose(); 
// I no longer want notifications
```

