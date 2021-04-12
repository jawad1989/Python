active = True

users = {}

while active:
    name = input("\n whats your name: ")
    age = input("your age: ")
    users[name] = age

    repeat = input("do you want to add more?")
    if (repeat == "n"):
        active = False
    elif repeat == "y":
        continue

for name, age in users.items():
    print(f"\n Hey {name}, ur {age}")
    