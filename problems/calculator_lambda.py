
def calculator(operation, num1, num2):
    return operation(num1, num2)


a = calculator(lambda n1, n2: n1 + n2, 10, 20)
s = calculator(lambda n1, n2: n1 - n2, 10, 20)
d = calculator(lambda n1, n2: n1 / n2, 10, 20)
m = calculator(lambda n1, n2: n1 * n2, 10, 20)
print(r)