import requests
import re
import json

#头部信息
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

#获取网页信息
def get_qishu_page(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text

#匹配正则获取小说信息
def parse_one_page(html):
    #获取作者<div.*?listBox.*?s.*?>(.*?)</div>
    pattern = re.compile('<div.*?s.*?>(.*?)</div>',re.S)
    items = re.findall(pattern,html)
    print(items)

#主方法
def main():
    url = 'https://www.qisuu.la/soft/sort01/'
    html = get_qishu_page(url)
    # print(html)
    parse_one_page(html)


main()