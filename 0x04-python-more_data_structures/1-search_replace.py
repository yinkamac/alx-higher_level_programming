#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for i, value in enumerate(new_list):
        if value == search:
            new_list[i] = replace
    return new_list
