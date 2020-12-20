def fib(num):
    """Approach 1: using list and without temp"""
    my_list = []
    for i in range(0, num):
        if i == 0 or i == 1:
            my_list.append(i)
        else:
            my_list.append(my_list[i-1]+my_list[i-2])
    return my_list


def fib_2(num):
    """Approach 2: using list and using a temp var"""
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp+a
    return result


# a = fib(20)
print(fib_2(21))


def fib_gen(num):
    """Approach 3: using Generators"""
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


# for item in fib_gen(20):
#     print(item)

def fib_rec(n):
    """Approach 4: using recursion"""
    if n == 0:
        print("in correct input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)


print(fib_rec(21))
