

def square(n):
    return n*n

def add_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += square(i)
    return total

test = 4

print(add_squares(test))


def test1(z):
    return 2*test(z - 1)

def test(n):
    if n == 0:
        return 0
    else:
        return test1(n - 1) + 1

print(test1(3))


