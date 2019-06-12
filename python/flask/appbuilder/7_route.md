## 路由：

### falsk 路由：

```
app = Flask(__name__)
@app.route("/ping")
def  ping():
    return "OK"
    pass
   
# 通过@app.route 注册路由
# 参考： http://docs.jinkan.org/docs/flask/quickstart.html#quickstart
```

appbuilder 通过继承view 来实现路由

