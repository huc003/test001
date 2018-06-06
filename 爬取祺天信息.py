import requests
import re
import json
import time

#爬取祺天网页信息
def get_qtyd_page(url):
    response = requests.get(url)
    if response.status_code==200:
        return response.text

#正则匹配爬取信息
def parse_one_page(html):
    #爬取项目信息<h3.*?item-name.*?>.*?a.*?>(.*?)</a>
    #项目链接.*?<h3.*?item-name.*?>.*?a.*?href="(.*?)"
    #年利率.*?item-apr.*?ft24.*?>(.*?)</em>
    #项目金额.*?item-sum.*?>(.*?)</span>
    #还款日期.*?item-refund.*?>(.*?)</span>
    #投资进度.*?item-speed.*?>(.*?)</i>
    #标状态.*?item-invset.*?a.*?>(.*?)</a>
    pattern = re.compile('<h3.*?item-name.*?>.*?a.*?href="(.*?)">(.*?)</a>'
                         '.*?item-apr.*?ft24.*?>(.*?)</em>'
                         '.*?item-sum.*?>(.*?)</span>'
                         '.*?item-refund.*?>(.*?)</span>.*?item-speed.*?>(.*?)</i>'
                         '.*?item-invset.*?a.*?>(.*?)</a>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            '标ID': item[0].strip()[8:13],
            '标链接': 'https://www.qtyd.com'+item[0].strip(),
            '标名称': item[1].strip(),
            '年利率': item[2].strip(),
            '标金额': item[3].strip()[1:],
            '还款日期': item[4].strip(),
            '投资进度': item[5].strip()[0:6].strip('<>') if item[5].strip()[0:6] != "100.00" else item[5].strip()[0:6]+"%",
            '标状态': item[6].strip()
        }

#写入文件
def write_to_json(content):
    with open('qtyd.txt','a',encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(page):
    url = "https://www.qtyd.com/invest/index-"+str(page)+".html"
    html = get_qtyd_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_json(item)

if __name__ == '__main__':
    for i in range(1):
        main(i+1)