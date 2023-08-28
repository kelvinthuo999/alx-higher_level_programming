#!/usr/bin/python3
""" function that divides element by element 2 lists """


def list_division(my_list_1, my_list_2, list_length):
    end_list = []
    try:
        for i in range(list_length):
            try:
                division_ans = my_list_1[i] / my_list_2[i]
            except (ZeroDivisionError):
                division_ans = 0
                print("division by 0")
            except (TypeError, ValueError):
                division_ans = 0
                print("wrong type")
            except (IndexError):
                division_ans = 0
                print("out of range")
            finally:
                end_list.append(division_ans)
    finally:
        return (end_list)
