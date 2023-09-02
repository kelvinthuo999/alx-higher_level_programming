def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float (default is 98).

    Returns:
        int: The addition of a and b as integers.

    Raises:
        TypeError: If a is not an integer or float, or if b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    result = a + b

    return round(result)
