import requests
import re

r = requests.get("https://www.qtyd.com/invest/index-2.html")
pattern = re.compile('<dd.*?invset-item.*?<h3.*?item-name.*?title="(.*?)">(.*?)</a>',re.S)
str = re.findall(pattern,r.text)
print(str)
#
# r2 = requests.get("https://www.qtyd.com/invest/index-2.html")
# pattern2 = re.compile('<li></li>',re.S)
# str2 = re.findall(pattern2,r2.text)
# print(str2)