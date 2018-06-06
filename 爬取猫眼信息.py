import requests
import re
import json
import time

#头部信息
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

#获取网页信息
def get_one_page(url):
    #通过get获取网页数据
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        #响应状态为200返回数据
        return response.text
    return None

#抓取到的信息写入文件
def write_to_json(content):
    with open('result.txt','a', encoding="utf-8") as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

#执行总方法
def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    parse_one_page(html)
    for item in parse_one_page(html):
        print(item)
        write_to_json(item)

#根据网页内容抓取信息
def parse_one_page(html):
    #获取排名<dd>.*?board-index.*?>(.*?)</i>
    #获取电影图片.*?data-src="(.*?)"
    #获取电影名称.*?name.*?a.*?>(.*?)</a>
    #获取电影主演.*?star.*?>(.*?)</p>
    #获取上映时间.*?releasetime.*?>(.*?)</p>
    #获取电影评分.*?i.*?integer.*?>(.*?)</i>
    #获取电影评分.*?i.*?fraction.*?>(.*?)</i>
    #结束.*?</dd>
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>'
                         '.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>'
                         '.*?star.*?>(.*?)</p>'
                         '.*?releasetime.*?>(.*?)</p>'
                         '.*?i.*?integer.*?>(.*?)</i>'
                         '.*?i.*?fraction.*?>(.*?)</i>'
                         '.*?</dd>',re.S)
    items = re.findall(pattern,html)

    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[4:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }

#循环爬取信息
if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)