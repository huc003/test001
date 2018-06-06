import urllib.request

response = urllib.request.urlopen('https://www.qtyd.com')
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))