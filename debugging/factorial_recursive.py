#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Computes the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer for which the factorial is calculated.

    Returns:
        int: The factorial value of the given integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)

