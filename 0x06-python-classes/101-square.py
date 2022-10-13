#!/usr/bin/python3
"""my square module."""

class Square:
    """define a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """ initialize the square with this
        Args:
            size: a side of square
            position: where the square is (coordinates)
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property of the length of a side of square
        Raises:
            TypeError: if size is not an int.
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of square
        Args:
            value: the size
        Raises:
                TypeError: if value is not int
                ValueError: if valie < 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property of the position of square
        Raises:
            TypeError: if value != tuple of 2 ints >= 0.
        Returns: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position
        Args:
            value: where
        Raises:
                TypeError: if not tuple, ints, positive
        Returns: the position
        """
        errMsg = TypeError("position must be a tuple of 2 positive integers")

        if type(value) is not tuple or len(value) != 2:
            raise errMsg
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise errMsg
        elif value[0] < 0 or value[1] < 0:
            raise errMsg

        self.__position = value

    def area(self):
        """ the area of square
        Returns:
            size * size
        """
        return self.__size ** 2

    def my_print(self):
        """returns the printed square with position"""
        printSize = self.__size
        if printSize == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(printSize):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(printSize):
                    print("#", end="")
                print()

