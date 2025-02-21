def Fib_rec(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    return Fib_rec(n - 1) + Fib_rec(n - 2)

print(Fib_rec(7))