#!/usr/bin/python3
""" function to generate Pascal's triangle """


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of list of int: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Generate the current row based on the previous row
        prev_row = triangle[-1]
        current_row = [1]  # First element of each row is always 1

        for j in range(1, i):
            current_element = prev_row[j - 1] + prev_row[j]
            current_row.append(current_element)

        current_row.append(1)  # Last element of each row is always 1
        triangle.append(current_row)

    return triangle
