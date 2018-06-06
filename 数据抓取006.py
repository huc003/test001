import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

def get_one_page_html(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?alt.*?src="(.*?)".*?name"><a'
               +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
               +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)# .可以匹配任意的换行符

    items = re.findall(pattern,html)
    #('1', 'http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c', '霸王别姬', '\n                主演：张国荣,张丰毅,巩俐\n        ', '上映时间：1993-01-01(中国香港)', '9.', '6'),
    for item in items:
        yield {
            'index' : item[0],
            'image' : item[1],
            'title':item[2],
            'actor' : item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score' : item[5] + item[6]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8')as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')#导入快捷见alt+enter,content内容是个字典，我们要把它变成字符串写入文件,加入换行符，每行一个
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page_html(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)  #会变成unicode编码，若想result.txt里面是中文,需要修改write_to_file函数，加上encoding=‘utf-8’和ensure_ascii=False

if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)

    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])