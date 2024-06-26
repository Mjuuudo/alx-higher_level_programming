#!/bin/usr/python3
class Square :
    def __init__(self, size = 0):
        self.__size = size
        
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
    def area(self):
        return self.__size ** 2
    def my_print(self):
        i = 0
        j = 0
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            j = 0
            print()