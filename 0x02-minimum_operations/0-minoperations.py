#!/usr/bin/python3
"""The Minimum Operations Challenge"""


def min_operations_to_get_n_h(n):
    """Computes the minimum operations"""
    if not isinstance(n, int):
        return 0

    operations_count = 0
    clipboard_size = 0
    current_characters = 1

    while current_characters < n:
        if clipboard_size == 0:
            # Initialize clipboard and perform the
            # first copy all and paste operation
            clipboard_size = current_characters
            current_characters += clipboard_size
            operations_count += 2
        elif n - current_characters > 0 and \
                (n - current_characters) % current_characters == 0:
            # Copy all and paste operation
            clipboard_size = current_characters
            current_characters += clipboard_size
            operations_count += 2
        elif clipboard_size > 0:
            # Paste operation
            current_characters += clipboard_size
            operations_count += 1

    return operations_count
