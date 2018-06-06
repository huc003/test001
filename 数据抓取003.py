import requests
import re

#获取网页
r = requests.get("https://www.qtyd.com/invest/index-2.html");
#定义正则
pattern = re.compile('<h3.*?item-name.*?title="(.*?)">(.*?)</a>',re.S);
#匹配正则
str = re.findall(pattern,r.text)
print(str)