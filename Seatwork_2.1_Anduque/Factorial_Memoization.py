#Implementation of Fibonacci Series using Memoization
""" The Fibonacci Series is a series of numbers in which each number
    is the sum of the preceding two numbers.
    By definition, the first two numbers are 0 and 1.

    Implement with the following steps:
    - Declare function with parameters: Number N and Dictionary Memo.
    - If n equals 1, return 0
    - If n equals 2, return 1
    - If current element is not in memo, add to memoy by recursive call for previous function and add. """


#Implementation of Factorial of a number N using Memoization

def Factorial(n, memo = {}):
  if n == 1: #base case
    return 1
  if not n in memo: #if the number input is not inside the dictionary
    memo[n] = n * Factorial(n-1) #add a update the dictionary with key of the input number and value of factorial by performing recursion

  return memo[n] #return the value of given key from the dictionary

print(Factorial(5))
#120