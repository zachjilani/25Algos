

def square(n):
    return n*n

def add_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += square(i)
    return total

test = 4

print(add_squares(test))



