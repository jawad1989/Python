import sys
import random

first   = int(sys.argv[1])
second  = int(sys.argv[2])

# first = int(a)
second = int(b)

rand_num = random.randint(first, second)

print(rand_num)

while True:
    a = int(input(f"guess number between {first} and {second}: "))
    if a == rand_num:
        print("you won")
        break
    else:
        print("wrong number")


# while True:
#     try:
#         guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
#         if  0 < guess < 11:
#             if guess == answer:
#                 print('you are a genius!')
#                 break
#         else:
#             print('hey bozo, I said 1~10')
#     except ValueError:
#         print('please enter a number')
#         continue