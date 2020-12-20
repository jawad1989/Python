import json

filename = 'json/username3.json'


def get_stored_username():
    # filename = 'json/username.json'
    try:
        with open(filename, 'r') as f:
            username = json.load(f)

    except FileNotFoundError:
        return None

    else:
        return username


def get_new_username():
    username = input("whats your username? ")
    # filename = 'json/username3.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"welcome back {username}")
    else:
        username = get_new_username()
        print(f"hi we will remember you {username}")


greet_user()
