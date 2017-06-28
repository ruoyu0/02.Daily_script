## windows下使用waitress运行app

#### 访问app1程序的`````\hello````` api:
```angular2html
http localhost:8000/hello # 200
```

#### 访问app2程序的api：
```angular2html
http localhost:8000/bookshelf # 结果：200
http localhost:8000/bookshelf/init_book # 结果：200
http localhost:8000/bookshelf/other_book # 结果：400
http POST localhost:8000/bookshelf  < test.json # 结果：待定
http localhost:8000/bookshelf # 结果：200
http DELETE localhost:8000/bookshelf/book3 # 结果：200
http localhost:8000/bookshelf # 结果：200
```


#### 访问app3_image的api：
```
http POST localhost:8000/images Content-type:image/jpeg < test.jpg
```