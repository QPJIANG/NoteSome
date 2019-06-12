国际化

参考： https://www.cnblogs.com/Ray-liang/p/4987455.html

```
#!/bin/bash
CURRENT_DIR=$(cd `dirname $0`;pwd)

pybabel extract -F babel/babel.cfg -o babel/messages.pot .

pybabel init -i babel/messages.pot -d app/translations -l zh

pybabel compile -d app/translations

pybabel update -i babel/messages.pot -d app/translations
```

