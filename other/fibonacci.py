
def fib():
    a = 0
    b = 1
    while True:
        c = a
        a = b
        b = c + a
        yield c

f = fib()

for i in range(8):
    print(next(f))