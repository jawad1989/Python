# # Developer: Jawad Saleem
# # Date: Dec, 7th, 2020
# # Description: undestranding lists in python
# # Actions: input, typecast, modulo operator, while loop(break, flag,)
# #          continue in while, moving list to another using while
# #          removing instances of particular value using while loop
# #          filling a dictionary using while

# # input number
# # age = input("whats your age?\n")
# # born_in = 2020 - int(age)
# # print(f"you were born in: {born_in}")

# # modulo/remainder
# number = 101
# result = number % 10
# print(result)

# # while loop
# counter = 0
# while counter <= 10:
#     print(counter)
#     counter += 1

# # while loop using a flag
# counter = 0
# active = True
# while active:
#     if counter == 7:
#         active = False
#     print(counter)
#     counter += 1

# # while loop, using break to exit loop
# while True:
#     print("number is:", counter)
#     if(counter == 15):
#         break
#     counter += 1


# # continue, in while loop to print odd numbers
# counter = 0
# while counter < 10:
#     counter += 1
#     if counter % 2 == 0:
#         continue
#     print(counter)


# # Moving items from one list to another
# unconfirmed_users = ['jawad', 'rajab', 'ahmad']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     confirmed_users.append(current_user)

# for user in confirmed_users:
#     print(user)


# # remove instances of specific value
# pets = ['dog', 'cat', 'turtle', 'snake', 'turtle',
#         'snake', 'turtle', 'snake', 'turtle', 'snake']
# print(pets)

# while 'snake' in pets:
#     pets.remove('snake')

# print(pets)

# filling a dictionary using while

polling_active = True
users = {}

while polling_active:
    name = input("\nwhats your name: ")
    age = input("your age: ")
    users[name] = age

    repeat = input("do you want to add more records? press (y) or (n): ")
    if repeat == "n":
        polling_active = False
    elif repeat == "y":
        continue

for name, age in users.items():
    print(f"\nHey {name}, you are {age} years old!")
