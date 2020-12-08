
def highest_even(li):
    even_numbers = []
    for n in li:
        if n % 2 == 0:
            even_numbers.append(n)
    return max(even_numbers)


print(highest_even([10, 2, 3, 4, 8, 11]))
