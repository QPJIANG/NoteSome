span 换行,但不截断单词
```css
span{
	white-space: normal;
	word-break:break-all;  
}

```





css 熟悉说明：

```
white-space 属性设置如何处理元素内的空白 

white-space: normal|pre|nowrap|pre-wrap|pre-line|inherit; 

normal默认。空白会被浏览器忽略。 
pre 空白会被浏览器保留。其行为方式类似 HTML 中的 pre 标签。 
nowrap文本不会换行，文本会在在同一行上继续，直到遇到 br 标签为止。 
pre-wrap 保留空白符序列，但是正常地进行换行。 
pre-line 合并空白符序列，但是保留换行符。 
inherit 规定应该从父元素继承 white-space 属性的值。

----------------------------------------------------------------
word-wrap 属性用来标明是否允许浏览器在单词内进行断句

word-wrap: normal|break-word; 

word-wrap 属性用来标明是否允许浏览器在单词内进行断句

normal: 只在允许的断字点换行(浏览器保持默认处理) 
break-word:在长单词或URL地址内部进行换行，
/*内容将在边界内换行。如果需要，单词内部允许断行。*/
----------------------------------------------------------------	
word-break 属性用来标明怎么样进行单词内的断句

word-break: normal|break-all|keep-all;

normal：使用浏览器默认的换行规则。 
break-all:允许在单词内换行 ， 允许任意非CJK(Chinese/Japanese/Korean)文本间的单词断行。
keep-all:只能在半角空格或连字符处换行，
不允许CJK(Chinese/Japanese/Korean)文本中的单词换行，只能在半角空格或连字符处换行。非CJK文本的行为实际上和normal一致。
```

