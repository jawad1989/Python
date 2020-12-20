import json

filename = 'json/username.json'

try:
    with open(filename, 'r') as f:
        username = json.load(f)
except FileNotFoundError as err:
    username = input("whats your username? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"hi we will remember you {username}")
else:
    print(f"welcome back {username}")
