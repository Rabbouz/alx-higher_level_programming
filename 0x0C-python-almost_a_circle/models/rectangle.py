#!/usr/bin/python3
"""Rectangle class(chile)."""
from models.base import Base #importing Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle.

        Args:
            width(int) : width of rectangle
            height(int) : height of rectangle
            x (int): x coordinate of the new Rectangle.
            y (int): y coordinate of the new Rectangle.
            id : the identity of rectangle
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """set/get of width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get of height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set/get of height of rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get y as coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get y as coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
