 
def add_nums(num1, num2):
    return int(num1) + int(num2)

def sub_nums(num1, num2):
    return int(num1) - int(num2)

def mul_nums(num1, num2):
    return int(num1) * int(num2)

def div_nums(num1, num2):
    return int(num1) / int(num2)


a = input("enter number a: ")
b = input("enter number b: ")

choice = input("what do you want to do? 1=+ , 2=-, 3=*, 4=/")

if(choice == "+"):
    print(add_nums(a,b))
elif(choice == "-"):
    print(sub_nums(a,b))
elif(choice == "*"):
    print(mul_nums(a,b))
elif(choice == "/"):
    print(div_nums(a,b))
