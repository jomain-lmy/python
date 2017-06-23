import urllib
import urllib.request
import io  
import sys  
import re 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

data={}
url = "http://jwc.ahu.cn/main/index.asp"
data = urllib.request.urlopen(url).read()
data=data.decode('gb2312','ignore')
# print(data)
# a="title='.*?>"
be = re.findall("title='.*?>",data)
# for x in be:
for x in be:
    bc = re.search("(title)='(.*?)'>",x, re.M|re.I)
    print(bc.group(2))

 
