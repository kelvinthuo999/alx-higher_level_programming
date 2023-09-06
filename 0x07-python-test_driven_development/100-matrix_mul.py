#!/usr/bin/python3
""" function that multiplies two matricess """


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices, m_a and m_b.

    Args:
        m_a (list of lists): The first matrix represented as a list of lists.
        m_b (list of lists): The second matrix represented as a list of lists.

    Returns:
        list of lists: The resulting matrix of the multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
        contains non-numeric elements, or has rows of varying lengths.
        ValueError: If m_a or m_b is empty
        or cannot be multiplied due to incompatible dimensions.
    """

    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list)
            for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists
                or m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) 
            for row in m_a for num in row) 
    or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers 
                or floats or m_b should contain only integers or floats")

    # Validate that m_a and m_b are rectangular matrices
    a_row_lengths = [len(row) for row in m_a]
    b_row_lengths = [len(row) for row in m_b]

    if len(set(a_row_lengths)) > 1 or len(set(b_row_lengths)) > 1:
        raise TypeError("Each row of m_a must 
                be of the same size or each row of m_b must be of the same size")

    # Validate that m_a's number of columns is equal to m_b's number of rows
    if len(m_a[0]) != len(b_row_lengths):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum_product = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(sum_product)
        result.append(row)

    return result
