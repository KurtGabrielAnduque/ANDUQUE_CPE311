#Implementation of Fibonacci Series using Tabulation
""" Fibonacci Series can be implemented using Tabulation using the following steps:
    - Declare the function and take the number whose Fibonacci Series is to be printed.
    - Initialize the list and input the values 0 and 1 in it.
    - Iterate over the range of 2 to n+1.
    - Append the list with the sum of the previous two values of the list.
    - Return the list as output. """

#Implementation of Factorial of a number N using Tabulation

def Factorial(n):
  table = [1] #create a table that will store products of n!
  for i in range(1, n+1): #perform iteration
    table.append(i * table[i-1]) #append a new value to table by multiplying to previous index
  return table[n] #return product of n index from the table


print(Factorial(5))
#120