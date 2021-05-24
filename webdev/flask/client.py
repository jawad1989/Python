import requests
#https://swapi.dev/about
url = 'http://127.0.0.1:5500/webdev/venv/server.py'
res = requests.get(url)
# print(dir(res))
print(res.content)
# print(res.iter_content)
print(res.text)
# print(dir(res))