try:
    answer = 25/5
except ZeroDivisionError as err:
    print(f"cant divide by zero\n{err}")
else:
    print(answer)
