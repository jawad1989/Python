num_a = 10


def my_func():
    global num_a
    num_a += 1
    print(num_a)


my_func()

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print(bool(0))

fruits = ["apple", "banana", "cherry"]
fruits[1] = "lemon"
print(fruits)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(
    car.get("model")
)
