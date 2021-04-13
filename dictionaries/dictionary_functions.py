# https://www.w3schools.com/python/python_ref_dictionary.asp
# clear, copy, fromkeys, get, itens, keys, pop, popitem, setdefault, update, values
dict_a = {
    'make': 'toyota',
    'price': 20
    }

dict_b = {
    'Toyota': {
        'model': "camry",
        'price': 20,
        'trim': 'XSE'
    },
    'Hona': {
        'model': 'civic',
        'price': 15,
        'trim': 'SE'
    }
}

## from keys
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

thatdict = dict.fromkeys(x)
print(thatdict)

## UPDATE
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

## pop item
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)