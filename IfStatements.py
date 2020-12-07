# Developer: Jawad Saleem
# Date: Dec, 7th, 2020
# Description: undestranding if Statements in python
# Actions: if,elif,else, booleans, check list is empty

n = 2
if(n == 3):
    print("im in")
elif(n == 2):
    print("im in elif")
else:
    print("nothing matched")

# and or
if(1 == 1 and 2 == 2):
    print("and checks passed")

if(1 == 1 or 1 == 3):
    print("or checks passed")

# checking if value is in list

my_list = [1, 2, 3, 4, 5, 6, 7, 6]
if 6 in my_list:
    print("number found")
else:
    print("not found")


banned_users = ["mike", "john", "sara"]
user = "peter"
if user not in banned_users:
    print(f"{user.title()}, you are not in banned list")


# boolean
game_actibe = True
can_edit = False

empty_list = []
# check if list is empty
if empty_list:
    print("not empty")
else:
    print("list empty")
