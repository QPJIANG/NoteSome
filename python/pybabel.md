```
pybabel extract . -F babel.cfg -k _ -k _ko -k _t -o xxxxxxxxxxxx/locale/en_US.pot --copyright-holder="xxxx.xxxx" --project="xxxxx" --version=""


babel.cfg:
[python: src/xxxx/**.py]
[mako: src/xxxx/templates/**.mako]
encoding=utf-8

extensions=xxx,xxx2

默认encoding: ascii   模板中文不通过。
extensions=jinja2.ext.autoescape,jinja2.ext.with_,webassets.ext.jinja2.AssetsExtension
```

