import requests
import re
import json
import time

#爬取祺天网页信息
def get_qtyd_page(url):
    response = requests.get(url)
    if response.status_code==200:
        return response.text

#正则匹配信息
def parse_one_page(html):
    #获取电影图片<img.*?quic.*?_src="(.*?)"
    #电影名称链接.*?<ul.*?info-list.*?title.*?a.*?href="(.*?)".*?>(.*?)</a>
    #获取主演1.*?actor.*?a.*?href="(.*?)".*?>(.*?)</a>
    #获取主演2.*?a.*?href="(.*?)".*?>(.*?)</a>
    #播放次数.*?<li>(.*?)</li>
    pattern = re.compile('<img.*?quic.*?_src="(.*?)"'
                         '.*?<ul.*?info-list.*?title.*?a.*?href="(.*?)".*?>(.*?)</a>'
                         '.*?actor.*?a.*?href="(.*?)".*?>(.*?)</a>'
                         '.*?a.*?href="(.*?)".*?>(.*?)</a>.*?<li>(.*?)</li>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            '海报': "http:"+item[0].strip(),
            '播放链接': "http:" + item[1].strip(),
            '电影名称': item[2].strip(),
            '演员介绍': "http:"+item[3].strip()+"、"+"http:"+item[5].strip(),
            '主演': item[4].strip()+"、"+item[6].strip(),
            '播放次数': item[7].strip()
        }

def write_to_json(content):
    with open('youku.txt','a',encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

#http://list.youku.com/category/show/c_96_s_1_d_1_p_1.html?spm=a2h1n.8251845.0.0
#http://list.youku.com/category/show/c_96_s_1_d_1_p_2.html?spm=a2h1n.8251845.0.0
def main(page):
    url = "http://list.youku.com/category/show/c_96_s_1_d_1_p_"+str(page)+".html?spm=a2h1n.8251845.0.0"
    html = get_qtyd_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_json(item)

if __name__ == '__main__':
    for i in range(10):
        main(i+1)