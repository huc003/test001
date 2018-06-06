import requests
r = requests.get("https://www.qtyd.com/favicon.ico")
with open('favicon.ico','wb') as f:
    f.write(r.content)