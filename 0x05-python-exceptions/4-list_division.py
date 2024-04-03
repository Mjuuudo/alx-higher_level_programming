#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    printed = 0
    new_list = []
    for i in range (0, list_length) :
        try :
            new_list.append(my_list_1[i] / my_list_2[i])
            i += 1
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError :
            new_list.append(0)
            print("Wrong type")
        except  IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            printed += 1
    return (new_list)
    