def super_fun(*args, **kwargs):
    # print(args)
    # print(kwargs)
    
    total = 0
    for items in kwargs.values():
        total += items

    return sum(args) + total

print (super_fun(2,2,3,4,5, num1=5,num2=10))



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
