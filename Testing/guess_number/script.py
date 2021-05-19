import random

def guess_number(guess,answer):
    if 0 < guess < 11:
        if guess == answer:
            print("you got it--in guess number")
            return True
        else:
            print("wrong guess")
            return False

if __name__ == '__main__':
    answer = random.randint(1,10)
    while True:
        try:
            guess    = int(input("guess number between 1-10: "))
            solution = guess_number(guess,answer)
            if solution != False:
                break
        except ValueError:
            print("try again")
            continue
