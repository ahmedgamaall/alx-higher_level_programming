#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = my_list[:]
    if 0 <= idx < len(my_list):
        tmp[idx] = element
        return(tmp)
    return(my_list)
