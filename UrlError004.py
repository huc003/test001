import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://www.baidu.com',timeout=0.001)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print('time out')