#!/usr/bin/python3
"""Empty Rectangle module that defines Rectangle class
with private variables height and width
"""


class Rectangle:
    """Represents Rectangle class with validated width and height

    the width must be a positive integer to be accepted as a value
    and so is the height otherwise ValueError or TypeError may be raised.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes instance of a rectangle
        Args:
            width (int, optinal): is the specified width
            of the rectangle (default is 0).
            height (int): is the specified height
            if the rectangle with a default value 0.

        Raises:
            TypeError: if width or height are not integers.
            ValueError: if width or height are less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            int: the current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of the retangle's width.

        Args:
            value (int): the new width value.

        Raises:
            TypeError: if the value type is not in integer.
            ValueError: if the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A getter to the height of the rectangle

        Returns:
            height (int): the current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of the rectangle's height

        Args:
            value (int): the new rectangle height

        Raises:
            TypeError: if value is not an integer.
            ValueError: if the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function return the area of the rectangle
        by multiplying the width with the height

        Returns:
            int: the area of the rectangle with
            the previously specified width and height by multiplying them.
            """
        return self.__width * self.__height

    def perimeter(self):
        """function perimeter calculates the perimeter of the rectangle.

        Returns:
            int: the perimeter of the rectangle
            if the width or height is 0 returns 0.
            """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append(str(self.print_symbol))
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """This method prints the repr of class Rectangle it
        returns the instance of creating Rectangle with height and width."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """This function is supposed to print a message
        if object of class Rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
    def square(cls, size=0):
