import requests
import re
import json
from urllib import error

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

def get_jb51_page(url):
    response = requests.get(url,headers=headers)
    response.encoding='GBK'
    if response.status_code == 200:
        return response.text

def parse_one_page(html):
    #获取pdf名称top-tit.*?a.*?href="(.*?)">(.*?)</a>
    pattern = re.compile('top-tit.*?a.*?href="(.*?)".*?>(.*?)</a>',re.S)
    items = re.findall(pattern,str(html))
    for item in items:
        #找到pdf下载链接
        downloads = get_download(item[0].strip().strip('/books/.html'))
        yield {
            '获取分享码ID': "下载"+item[0].strip().strip('/books/.html'),
            '书名': item[1],
            '访问链接': "http://www.jb51.net"+item[0],
            '下载链接1': downloads[0][0].strip() if "/do/plus/download1.php" not in downloads[0][0].strip() else "http://www.jb51.net"+downloads[0][0].strip(),
            '下载链接2': downloads[0][1].strip() if "/do/plus/download1.php" not in downloads[0][1].strip() else "http://www.jb51.net"+downloads[0][1].strip()
        }

def get_download(id):
    response = requests.get("http://www.jb51.net/books/"+id+".html", headers=headers)
    pattern = re.compile('ul_Address.*?a.*?href="(.*?)".*?>.*?a.*?href="(.*?)".*?></a>', re.S)
    items = re.findall(pattern, response.text)
    return items

#152java
#476python
#482mysql
#300ajax
#18javascript
type = 152
def main(page,type):
    url = "http://www.jb51.net/books/list"+str(type)+"_"+str(page)+".html"
    html = get_jb51_page(url)
    for item in parse_one_page(html):
        print(item)

if __name__ == '__main__':
    for i in range(10):
        main(i+1,type)