"""
Module with one fib(n) function which searches for the nth
fibonacci number.
"""


def fib(n):
    """Searches for the nth fibonacci number."""
    if n < 0:
        print("Danger Will Robinson!")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
