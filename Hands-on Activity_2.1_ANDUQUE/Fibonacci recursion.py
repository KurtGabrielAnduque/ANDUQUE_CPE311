def Fib_rec(n):
    # base cases
    if n == 1:
        return 1
    if n == 2:
        return 1
    # perform recursive call
    return Fib_rec(n - 1) + Fib_rec(n - 2)

print(Fib_rec(7))