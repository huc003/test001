from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

username = 'test'
password = '123456'
url = 'http://192.168.0.8:9764/eureka-server/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handle = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handle)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)