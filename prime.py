"""
Module which contains 2 functions, is_prime(n) checks if a number is prime
and primes(n) which lists all primes under a given n.
"""


def is_prime(n):
    """Checks if n is prime and returns a True or False"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes(n):
    """Returns a list of all prime numbers under a given n"""
    prime_list = []
    for i in range(2, n+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list
