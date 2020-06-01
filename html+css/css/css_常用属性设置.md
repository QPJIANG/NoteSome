
盒子模型

```
四值顺序：top right bottom left 按顺时针方向，则left被缺省，其值等于right

Margin(外边距) - 清除边框外的区域，外边距是透明的。（margin,margin-left/right/top/bottom）
Border(边框) - 围绕在内边距和内容外的边框。
			(border: <厚度> <样式: border-style可单独设置> <颜色：border-color 可单独设置>)
			(border-top/right/bottom/left-style)
			border-style: 设置多个样式（遵守”四值顺序“）
Padding(内边距) - 清除内容周围的区域，内边距是透明的。(padding,padding-left/right/top/bottom)
Content(内容) - 盒子的内容，显示文本和图像 (width,height)


元素显示宽高占用：
总元素的宽度=宽度+左填充+右填充+左边框+右边框+左边距+右边距
总元素的高度=高度+顶部填充+底部填充+上边框+下边框+上边距+下边距

在设置元素宽为百分百时： 边距和边框将会导致出现横向滚动条。[即：百分比是相对container而言的。]

width
height
max-width
max-height
min-width
min-height
```

```
在元素上设置了 box-sizing: border-box; 则 padding(内边距) 和 border(边框) 也包含在 width 和 height 中
```

阴影

```
box-shadow
box-shadow: h-shadow v-shadow blur spread color inset;

h-shadow	必需的。水平阴影的位置。允许负值
v-shadow	必需的。垂直阴影的位置。允许负值
blur	可选。模糊距离
spread	可选。阴影的大小
color	可选。阴影的颜色。
inset	可选。从外层的阴影（开始时）改变阴影内侧阴影
```

背景：

```
background-color：
background-image：
```

文字：

```
color: 文字颜色


文本修饰
text-decoration: none; （a 标签去下划线）
none		默认。定义标准的文本。
underline	定义文本下的一条线。
overline	定义文本上的一条线。
line-through	定义穿过文本下的一条线。
blink		定义闪烁的文本。
inherit	规定应该从父元素继承 text-decoration 属性的值。

对齐
text-align： center/left/right/justify
	"justify"，每一行被展开为宽度相等，左，右外边距是对齐


大小写：
text-transform：uppercase/lowercase/capitalize

缩进
text-indent：  (px)


color	设置文本颜色
direction	设置文本方向。
letter-spacing	设置字符间距
line-height	设置行高
text-align	对齐方式
text-decoration	向文本添加修饰
text-indent	缩进元素中文本的首行
text-shadow	设置文本阴影
text-transform	控制元素中的字母
unicode-bidi	设置或返回文本是否被重写 
vertical-align	设置元素的垂直对齐
white-space	设置元素中空白的处理方式
word-spacing	设置字间距
```

弹性盒子：

```
display: flex;   作用在父容器上，子元素排列生效。   （父div设置，子div 平行排列）
```

圆角：

```
 border-radius 
 
 四个值: （top-left 开始，顺时针）
 三个值: 第一个值为左上角, 第二个值为右上角和左下角，第三个值为右下角 
 两个值: （top-left 开始，顺时针,交替生效）
 一个值： 四个圆角值相同
 
 弧度：
 
 
```

旋转

```
transform

-ms-transform:rotate(-8deg); /* IE 9 */
-webkit-transform:rotate(-8deg); /* Safari and Chrome */
transform:rotate(-8deg);
正数为顺时针旋转角度
```

调整元素尺寸：

```
resize： 指定一个元素是否应该由用户去调整大小
```

轮廓

```
outline （轮廓）是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用。

注释：轮廓线不会占据空间，也不一定是矩形。

outline 简写属性在一个声明中设置所有的轮廓属性。

可以按顺序设置如下属性：

outline-color
outline-style
outline-width
```

多列

```
column-count 列数
column-gap 指定列与列之间的间隙
column-rule-style	指定两列间边框的样式
column-rule-width	指定两列间边框的厚度
column-rule-color  指定两列间边框的颜色
column-rule		所有 column-rule-* 属性的简写
column-span		指定元素要跨越多少列
column-width	指定列的宽度
columns			设置 column-width 和 column-count 的简写
```

CSS3 动画

```

@keyframes	规定动画。
	用百分比来规定变化发生的时间
	用关键词 "from" 和 "to"，等同于 0% 和 100%。
	

animation	所有动画属性的简写属性，除了 animation-play-state 属性。	
animation-name	规定 @keyframes 动画的名称。	
animation-duration	规定动画完成一个周期所花费的秒或毫秒。默认是 0。	
animation-timing-function	规定动画的速度曲线。默认是 "ease"
animation-fill-mode	规定当动画不播放时（当动画完成时，或当动画有一个延迟未开始播放时），要应用到元素的样式。	
animation-delay	规定动画何时开始。默认是 0。	
animation-iteration-count	规定动画被播放的次数。默认是 1。	
animation-direction	规定动画是否在下一周期逆向地播放。默认是 "normal"。
animation-play-state	规定动画是否正在运行或暂停。默认是 "running"。	

```


浏览器样式前缀

```
-moz- ：Firefox，GEcko引擎
-webkit-： Safari和Chrome，Webkit引擎
-o- ：Opera（早期），Presto引擎，后改为Webkit引擎
-ms- ：Internet Explorer，Trident引擎
```

