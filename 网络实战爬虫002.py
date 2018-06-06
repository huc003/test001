import requests

r = requests.post('http://httpbin.org/post')
print(r)
r = requests.put('http://httpbin.org/put')
print(r)
r = requests.delete('http://httpbin.org/delete')
print(r)
r = requests.head('http://httpbin.org/get')
print(r)
r = requests.options('http://httpbin.org/get')
print(r)

r = requests.get('http://httpbin.org/get')
print(r.text)