import urllib
import urllib.request
import io  
import sys  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

data={}

data['word']='Jecvay Notes'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
data=data.decode('gb2312','utf-8')
print(data)
