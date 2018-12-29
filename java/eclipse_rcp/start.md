```
开发环境：
	eclipse 安装rcp 插件。 或使用集成好rcp 的eclipse.

参考：http://www.blogjava.net/youxia/archive/2006/11/17/81852.html
创建项目：

创建项目->Plugin-inDevelopment->Plugin-in project [next]
输入：项目名;选择eclipse 版本（3.5 or greater）;   [next]
选择 rich client application(yes)  [next]
选择 HELLO RCP	[finish]


run as : eclipse application  可直接运行出窗口。

创建产品配置：
new -> product configuration
输入： filename ; initialize the file content: with basic settings
general informations: 输入id version name
product Definition: new -> browser (查找创建的项目名)
					product application: 项目名.application
dependencies: add (查找创建的项目名并添加); add required plugin-ins

launch an eclipse application  可直接运行出窗口.

导出：
	选择导出路径，导出文件夹名称等 [finish]




GLib-CRITICAL **: XXXXX :assertion 'in != NULL' failed 

export SWT_GTK3=0

```

