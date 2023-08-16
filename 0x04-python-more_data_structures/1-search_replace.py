#!/usr/bin/python3
""" function to search and replace an element """


def search_replace(my_list, search, replace):
    new_list = []

    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    return (new_list)
