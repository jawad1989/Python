import json

username = input("whats your name? ")

filename = "json/username.json"

with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print(f"file written, {username}")
