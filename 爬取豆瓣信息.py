import requests
import re
import json
import time

#请求头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

#爬取豆瓣电影网页信息
def get_douban_page(url):
    response = requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text

def parse_one_page(html):
    # 获取主演.*?<li.*?list-item.*?>.*?data-actors="(.*?)"
    #获取电影名称.*?<li.*?stitle.*?>.*?stitle.*?a.*?>(.*?)</a>
    #获取图片.*?<li.*?poster.*?>.*?ticket-btn.*?src="(.*?)"
    #获取评分.*?<li.*?srating.*?>.*?span.*?subject-rate.*?>(.*?)</span>
    pattern = re.compile('<li.*?list-item.*?>.*?data-actors="(.*?)"'
                         '.*?<li.*?stitle.*?>.*?a.*?>(.*?)</a>'
                         '.*?<li.*?poster.*?>.*?ticket-btn.*?src="(.*?)"',re.S)
    # pattern = re.compile('<span.*?subject-rate.*?>(.*?)</span>', re.S)
    items = re.findall(pattern,html)

    for item in items:
        yield {
            'index': item[0],
            'title': item[1].strip(),
            'image': item[2].strip()
        }

def main():
    url = 'https://movie.douban.com/cinema/nowplaying/hangzhou/'
    html = get_douban_page(url)
    for item in parse_one_page(html):
        print(item)

main()
