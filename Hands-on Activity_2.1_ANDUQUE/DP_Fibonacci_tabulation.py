def DP_Fib(n):
    table = [0,1]
    for number in range(2,n + 1):
        table.append(table[number - 1] + table[number - 2])
    return table[n]
print(DP_Fib(7))