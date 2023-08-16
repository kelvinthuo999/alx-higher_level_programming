#!/usr/bin/python3
""" function to return weighted average """


def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_product = sum([score * weight for score, weight in my_list])
    sum_weights = sum([weight for _, weight in my_list])

    if sum_weights == 0:
        return 0

    return (sum_product / sum_weights)
