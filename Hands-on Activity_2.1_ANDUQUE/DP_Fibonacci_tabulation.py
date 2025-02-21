def DP_Fib(n):
    table = [0,1]
    #perform iteration for storing new result into a talbe
    for number in range(2,n + 1):
        #append the result to a table if the are not record from the table
        table.append(table[number - 1] + table[number - 2])
    return table[n]
print(DP_Fib(7))