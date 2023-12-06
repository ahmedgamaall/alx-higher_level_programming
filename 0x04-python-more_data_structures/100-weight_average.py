#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numbers = 0
    count = 0

    for number in my_list:
        numbers += number[0] * number[1]
        count += number[1]
    average = numbers / count
    return average
