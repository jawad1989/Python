""" check if brackets are balanced or not """

def check_balance(br):
    count = 0

    for b in br:
        if b == "]":
            count -= 1
        
        elif b == "[":
            count += 1
        
        if count < 0:
            break
    print(count)
    return count == 0

print(check_balance("[]"))