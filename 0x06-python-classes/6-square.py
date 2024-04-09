#!/bin/usr/python3
class Square :
    def __init__(self, size = 0, position=(0, 0)):
        self.__size = size
        self.__position = position
        
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        if not isinstance(size, int) :
            raise TypeError("size must be an integer")
        elif size < 0 :
            raise ValueError("size must be >= 0")
        else :
            self.__size = size

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) :
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 :
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or not isinstance(position[1], int) :
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0  or  position[1] < 0 :
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if (self.__size == 0) :
            print()
        else :
            for k in range(self.__position[1]):
                print()
                for i in range(self.__size):
                    for j in range(self.__position[0]):
                        print("#" * (self.__size))
                    print(" ", end="")
                    
            