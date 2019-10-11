.vscode/settings.json

```
// 一个文件使用一个tab
"workbench.editor.enablePreview": false     


// 文件菜单树不显示的文件/目录
"files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/__pycache__": true,
        "**/.DS_Store": true,
        "**/node_modules": true,
        "**/*.pyc": true
    }
```









快捷键设置:

File -> Perferience -> KeyboardShortcuts







```
//文件注释模板： psioniq File Header
   
"psi-header.templates": [
        {
            "language": "*",
            "template": [
                "FileName: <<filename>>",
                "Project: <<projectname>>",
                "",
                "Author: xxx@xxx.com",
                "File Created: <<filecreated('YYYY-MM-DD h:mm:ss ,dddd')>>",
                "",
                "Modified By: <<author>>",
                "Last Modified: <<dateformat('YYYY-MM-DD h:mm:ss ,dddd')>>",
                "",
                "Copyright (c) <<filecreated('YYYY')>> xxxxxxxxxx."
            ]
        }
    ],
"psi-header.lang-config": [
        {
            "language": "javascript",
            "begin": "",
            "end": "",
            "prefix": "// "
        },
        {
            "language": "python",
            "begin": "####################################################################################################",
            "end": "####################################################################################################",
            "prefix": "# ",
            "suffix":"#",
            "lineLength":100,
            "replace":[],
            "modAuthor":"Modified By: xxx@xxx.com",
            "modDate":"Last Modified: <<dateformat('YYYY-MM-DD h:mm:ss ,dddd')>>",
        }
    ],
"psi-header.changes-tracking":{
        "isActive":true,
        "modAuthor":"Modified By: xxx@xxx.com",
        "modDate":"Last Modified: <<dateformat('YYYY-MM-DD h:mm:ss ,dddd')>>",
        "autoHeader":"autoSave"
    },
```

