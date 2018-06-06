import requests

data = {
    'name':'hucheng',
    'age':24
}

r = requests.get('http://httpbin.org/get',params=data)
print(r.text)