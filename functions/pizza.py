def make_pizza(size, price, *toppings2):
    print(
        f"\nMaking {size} inches pizza, costing {price} with following toppings:")
    for topping2 in toppings2:
        print(f"- {topping2}")
