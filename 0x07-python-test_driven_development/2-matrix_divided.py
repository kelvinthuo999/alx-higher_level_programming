def matrix_divided(matrix, div):
    """
    Divides a matrix by a number and rounds to 2 decimal places.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: new matrix with elements divided and rounded to 2 dp.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if each row of the matrix does not have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to zero.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and
               all(isinstance(val, (int, float)) for val in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    # Check if div is a number (integer or float) and not equal to zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    return new_matrix
