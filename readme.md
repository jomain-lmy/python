[python]

用python写爬虫，保持网页到本地文件

## 方法

[data['word']='Jecvay Notes']

抓取百度上面搜索关键词为Jecvay Notes的网页

data是一个字典, 然后通过urllib.parse.urlencode()来将data转换为 'word=Jecvay+Notes'的字符串, 最后和url合并为full_url


## 问题
 2017.6.23 百度网页可以成功下载，从控制台储存到文件过程中出现中文字符乱码