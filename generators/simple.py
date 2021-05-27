def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
     print(char)

a = reverse("jawad")
print(next(a))
print(next(a))