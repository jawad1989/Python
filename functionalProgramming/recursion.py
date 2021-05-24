def num_zero(num):
    print("number: ", num)
    
    # base case
    if num == 0:
        print("zero reached")
    else:
       num_zero(num-1)

num_zero(5)

""" Fibonacci sequence using recursion """
def fib_rec(n):
    
    
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)

print(fib_rec(10))

""" factorial  using recursion """
def factorial(n):

    # base case
    if n == 0 or n ==1:
        return 1

    if n < 1:
        return -1

    # Recursion
    return n * factorial(n-1) 
    
print(factorial(5))
