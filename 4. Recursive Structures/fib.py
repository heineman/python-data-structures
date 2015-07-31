"""
    Recursive solution to Fibonacci. Truly inefficient.

    Author: George Heineman
"""
def fib(n):
  # Base case
  if n < 2: return 1

  # Action and Recursive Step
  return fib(n-1) + fib(n-2)
