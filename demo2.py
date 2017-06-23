import urllib.request

url = "http://jwc.ahu.cn/main/index.asp"
data = urllib.request.urlopen(url).read()
data = data.decode('gb2312')
print(data)