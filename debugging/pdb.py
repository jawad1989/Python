"""
commands to use while tracing using pdb
list 
w
a
"""
import pdb

def add(num1,num2):
    pdb.set_trace()
    return num1 + num2

sum = add (4,5)

print(f'SUM = {sum}')