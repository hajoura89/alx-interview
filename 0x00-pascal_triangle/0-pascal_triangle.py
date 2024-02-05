#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of
    integers representing Pascal’s triangle of n

    Args:
    - n (int): The number of rows for Pascal's Triangle.

    Returns:
    - List of lists: A list of lists representing Pascal's Triangle.
      Returns an empty list if the input is not a positive integer.
    """

    triangle = []  # Initialize an empty list to store the triangle

    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return triangle  # Return an empty list if n is not a positive integer

    # Iterate through each row of Pascal's Triangle
    for i in range(n):
        line = []  # Initialize an empty list for the current row
        for j in range(i + 1):
            # Check if the current element is at the beginning or end of row
            if j == 0 or j == i:
                line.append(1)  # If so, set the element to 1
            else:
                # If not, calculate the element by summing
                # the two elements from the previous row
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)  # Append the current row to the triangle list

    return triangle  # Return the final Pascal's Triangle
