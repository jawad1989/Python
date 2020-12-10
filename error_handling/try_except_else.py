# syntax, key, index,key, zeroDivsion, Type, value

# Error Handling
# This example only accepts int as an age
while True:
    try:
        age = int(input('whats ur age'))
        print(age)
        # 10/age
    except ValueError:
        print("enter valid input")
    except ZeroDivisionError:
        print("enter non 0 number")
    else:
        print("thank you")
        break
