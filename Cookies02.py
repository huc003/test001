import requests
headers = {
    'Cookie':''
}
r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)