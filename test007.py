import requests
import re

def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def main():
    url = 'https://www.qtyd.com/invest/index.html'
    html = get_one_page(url)
    # print(html)
    parse_one_page(html)

def parse_one_page(html):
    pattern = re.compile(
        '<h3.*?href="(.*?)".*?title="(.*?)">(.*?)</a>',re.S
    )
    items = re.findall(pattern, html)
    print(items)

main()

# .*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)'
#         '</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>