
class Com:
    def __init__(self, real=0, imag=0) -> None:
        self.real = real
        self.imag = imag

    def __add__(self, other):
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other):
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp

obj1 = Com(1,2)
obj2 = Com(10,5)

add = obj1 + obj2
sub = obj1 - obj2

print("real of obj3:", add.real)
print("imag of obj3:", add.imag)
print("real of obj4:", sub.real)
print("imag of obj4:", sub.imag)