#!/usr/bin/python3
def print_sorted_dictionary(my_dictionary):
    new_dictionary = sorted(my_dictionary.keys())
    for i in new_dictionary:
        print("{}: {}".format(i, new_dictionary[i]))
