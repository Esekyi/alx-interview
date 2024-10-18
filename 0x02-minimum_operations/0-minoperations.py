#!/usr/bin/python3
""" Likely interview algorithm question """


def minOperations(n: int) -> int:
    """ Minimum operations to reach number n"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n = n // divisor
        else:
            divisor += 1

    return operations
