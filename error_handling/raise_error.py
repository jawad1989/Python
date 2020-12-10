# sum of two numbers, both numbers should be int
def calc(num1, num2, op):
    try:
        if op == '+':
            return num1+num2
        elif op == '/':
            return num1/num2
        else:
            raise ValueError('hey stop it!!')
            # raise Exception('Hey Cut it out!!!')
            return "operation not defined"
    except (TypeError, ZeroDivisionError) as err:
        return f'Both numbers should be integers:\nError: {err}'
    # except ValueError:
    #     return 'My Value Error'
    else:
        return "im in else"


print(calc(10, 's', '*'))
