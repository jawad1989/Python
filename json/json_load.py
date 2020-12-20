import json

filename = 'json/json_write.json'

with open(filename) as f:
    data = json.load(f)

print(data)
print((data['user_a']))
