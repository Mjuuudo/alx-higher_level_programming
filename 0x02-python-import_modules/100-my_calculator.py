#!/usr/bin/python3
from calculator_1 import add,sub,mul,div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif  len(sys.argv) == 4:
        if sys.argv[2] == '+':
            res = add(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == '-':
            res = sub(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == '*':
            res = mul(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == '/':
            res = div(int(sys.argv[1]), int(sys.argv[3]))
        else :
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    print(f"{int(sys.argv[1]):d}", end=" ")
    print(f"{sys.argv[2]}", end=" ")
    print(f"{int(sys.argv[3]):d}", end=" ")
    print("=", end=" ")
    print(f"{res:d}", end=" ")
elif __name__ != "__main__":
    exit()
