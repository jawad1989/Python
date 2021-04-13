#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat_1 = Cat('Kitty', 3)
cat_2 = Cat('Tom', 15)
cat_3 = Cat('Max',   9)

# 2 Create a function that finds the oldest cat

# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {get_oldest_cat(cat_1.age, cat_2.age, cat_3.age)} years old.")
