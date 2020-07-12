template:

```
https://www.jetbrains.com/help/pycharm/file-template-variables.html


```

build in vars

```
${DATE}	 Current system date
${DAY}	Current day of the month
${DS}	Dollar sign $. This variable is used to escape the dollar character, so that it is not treated as a prefix of a template variable.
${FILE_NAME}	Name of the new file.
${HOUR}	Current hour
${MINUTE}	Current minute
${MONTH}	Current month
${MONTH_NAME_FULL}	Full name of the current month (January, February, and so on)
${MONTH_NAME_SHORT}	First three letters of the current month name (Jan, Feb, and so on)
${NAME}	Name of the new entity (file, class, interface, and so on)
${ORGANIZATION_NAME}	Name of your organization specified in the project settings (Ctrl+Shift+Alt+S)
${PRODUCT_NAME}	Name of the IDE (for example, PyCharm)
${PROJECT_NAME}	Name of the current project
${TIME}	Current system time
${USER}	Login name of the current user
${YEAR}	Current year
```

```
自定义变量：
在模板文件开头设置变量。
#set( $MyVarname = "var value" )
```

```
实例

#set( $MyName = "xxxx" )
#set( $DEV_VERSION = "xx.xxx" )

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@License :   xxxxx  
@File    :   ${NAME}.py
@Time    :   ${YEAR}/${MONTH}/${DAY} ${HOUR}:${MINUTE}
@Author  :   ${MyName} 
@Version :   ${DEV_VERSION}
@Contact :   ${MyName}@xxxx.com
@Desc    :   
'''
```

