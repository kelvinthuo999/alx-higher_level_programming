#!/usr/bin/python3
""" function that multiplies two matrices """


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices, m_a and m_b, using NumPy.

    Args:
        m_a (list of lists): The first matrix represented as a list of lists.
        m_b (list of lists): The second matrix represented as a list of lists.

    Returns:
        numpy.ndarray: The resulting matrix of the multiplication.

    Raises:
        ValueError: If m_a or m_b is not a valid matrix for multiplication.
    """

    try:
        result = np.dot(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
