import bisect

A = [-14, -10, 2, 108, 240, 243, 285, 285, 285, 401]
print(A)
print("Length =", len(A))
# print(find_duplicate(A))

# -10 is at index 1.
print("")
print(bisect.bisect_left(A, -10))
print(bisect.bisect_right(A, -10))
print(bisect.bisect(A, -10)) 

# first occurance of 285 is at index 6
print("")
print(bisect.bisect_left(A, 285))
print(bisect.bisect_right(A, 285))
print(bisect.bisect(A, 285)) 

# Not found
print("")
print(bisect.bisect_left(A, -14))
print(bisect.bisect_right(A, -14))
print(bisect.bisect(A, -14)) 

# Not found
print("")
print(bisect.bisect_left(A, -115))
print(bisect.bisect_right(A, -115))
print(bisect.bisect(A, -115)) 