class Dog:
    """A simple attempt to model a Dog"""

    def __init__(self, name, age):
        """initilize name and age """
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting """
        print(f"{self.name}, is now sitting")

    def roll_over(self):
        """Simulate a rollover"""
        print(f"{self.name}, rolled over")


my_dog = Dog('Max', 6)
print(f"My dog name is {my_dog.name}")
my_dog.roll_over()
my_dog.sit()

my_dog = Dog('Lucy', 10)
print(f"\nMy dog name is {my_dog.name}")
my_dog.roll_over()
my_dog.sit()
