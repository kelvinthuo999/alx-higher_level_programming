#!/usr/bin/python3
""" definition of class MyInt """


class MyInt(int):
    """ definition of class MyInt """
    def __eq__(self, other):
        """
        Overrides the equality (==) operator.
        Args:
            other: The value to compare with.
        Returns:
            bool: True if the values are not equal,
            False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality (!=) operator.
        Args:
            other: The value to compare with.
        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
