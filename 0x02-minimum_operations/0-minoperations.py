#!/usr/bin/python3
"""The Minimum Operations Challenge"""


def minOperations(n):
    if n == 1:
        return 0  # Already have one 'H'

    operations = 0
    clipboard = 0

    for i in range(2, n + 1):
        if n % i == 0:
            clipboard = i
            operations += 2  # Copy All and Paste

            while n % clipboard == 0:
                n //= clipboard
                operations += 1  # Paste

    return operations if n == 1 else 0


