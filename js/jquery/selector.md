##  -  通配符：

	$("input[id^='code']");//id属性以code开始的所有input标签
	$("input[id$='code']");//id属性以code结束的所有input标签
	$("input[id*='code']");//id属性包含code的所有input标签
	$("input[name^='code']");//name属性以code开始的所有input标签
	$("input[name$='code']");//name属性以code结束的所有input标签
	$("input[name*='code']");//name属性包含code的所有input标签


##  - 

	$("tbody tr:even"); //选择索引为偶数的所有tr标签
	$("tbody tr:odd"); //选择索引为奇数的所有tr标签
	$(".main > a"); class为main的标签的子节点下所有标签
	jqueryObj.next("div");//获取jqueryObj标签的后面紧邻的一个div，nextAll获取所有
	//not
	$("#code input:not([id^='code'])");//id为code标签内不包含id以code开始的所有input标签
