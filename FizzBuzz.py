# take an input
n = int(input())
# loop from 1 to n odd numbers
for x in range(1, n, 2):
    if x % 3 == 0 and x % 5 == 0:
    # if number is multiple of 3 and 5
        print("Danish Khan")
    elif x % 3 == 0:
    # if number is multiple of 3
        print("Danish")
    elif x % 5 == 0:
    # if number is multiple of 5
        print("Khan")
    else:
    # otherwise print number
        print("Hello!")