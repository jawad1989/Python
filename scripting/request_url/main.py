import requests
#https://swapi.dev/about
url = 'https://jsonplaceholder.typicode.com/posts'
res = requests.get(url)
print(dir(res))
print(res.content)
print(res.iter_content)
print(res.text)
print(dir(res))