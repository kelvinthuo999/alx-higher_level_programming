#!/usr/bin/python3
""" a class to define a rectangle """


class Rectangle:
    """
    Rectangle class defines a rectangle by its width and height.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance
        with optional width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle.
        Returns:
            str: A string containing the rectangle's shape
            with the character(s) stored in print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
                [str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """
        Return a string representation of the rectangle for recreation.

        Returns:
            str: A string that can be used with eval() to recreate the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor method to print a message when an instance
        is deleted and decrement the number_of_instances attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method to return the bigger rectangle based on the area.
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        Raises:
            TypeError: If either rect_1
            or rect_2 is not an instance of Rectangle.
        Returns:
            Rectangle: The rectangle with the larger area,
            or rect_1 if they have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 >= area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method to create a new square Rectangle instance.

        Args:
            size (int): The size of the square (default is 0).

        Returns:
            Rectangle: A new Rectangle instance where width
            and height are equal to size.
        """
        return cls(size, size)
