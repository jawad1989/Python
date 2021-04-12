def greet_users(names):
    """ Pass list to function"""
    new_users = []
    while names:
        current_name = names.pop()
        print("current item:", current_name)
        new_users.append(current_name)

    for x in new_users:
        print(f"Hello {x}")

names = ["jawad", "rajab", "ahmad"]

greet_users(names)