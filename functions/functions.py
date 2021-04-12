# arguments and params
# default values
# using slice notation[:] to send a copy of list to function
# mixing position and arbitrary argument

# sum of two numbers
def sum(a, b=10):
    """function to add two numbers"""
    return a+b


print("sum is:", sum(1, 2))
print("sum is:", sum(2, 2))
print(sum(1))


# function with optional param
def add(a, b, c=0):
    return a+b+c


print("Sum is = ", add(1, 2, 3))
print("Sum is = ", add(1, 2))

# Returning a dictionary


def build_person(f_name, l_name):
    """Returns a dictionary of information about a person"""
    person = {'first': f_name, 'last': l_name}
    return person


musician = build_person('jawad', 'saleem')
print(musician)


# Retun age of person from dictionary

def return_age(name):
    users = {
        'jawad': 31,
        'rajab': 26
    }

    for key, value in users.items():
        if key == name:
            return value
    return False


get_age = return_age('jawad')
if get_age:
    print("Age is:", get_age)
else:
    print("user not found")


# passing a list
def greet_users(names):
    """Pass list to function"""
    new_names = []
    while names:
        current_name = names.pop()
        print("current item:", current_name)
        new_names.append(current_name)

    for name in new_names:
        print(f"Hello, {name}")


names = ['jawad', 'rajab', 'ahmad']

greet_users(names[:])
print("post:", names)


# Arbitrarys number of arguments
def make_pizze(*toppings):
    """prints all requested toppigs"""

    for topping in toppings:
        print(f"- {topping}")


list_a = ('cheese')
list_b = ('cheese', 'chicken', 'mushrooms', 'olives')
list_c = ['beef', 'chicken', 'mushrooms', 'olives']
make_pizze(list_a)
make_pizze(list_b)
make_pizze(list_c)


# mixing position and arbitrary argument

def make_pizza_2(size, price, *toppings2):
    print(
        f"\nMaking {size} inches pizza, costing {price} with following toppings:")
    for topping2 in toppings2:
        print(f"- {topping2}")


make_pizza_2(16, 20, 'cheese')
make_pizza_2(7, 10, 'cheese', 'chicken', 'beef')


def build_profile(f_name, l_name, ** user_info):
    user_info['f_name'] = f_name
    user_info['l_name'] = l_name
    return user_info


user_profile = build_profile('jawad', 'saleem', location='austin', age=31)

print(user_profile)
