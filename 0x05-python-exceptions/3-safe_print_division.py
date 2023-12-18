#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divition = a / b
    except (TypeError, ZeroDivisionError):
        divition = None
    finally:
        print("Inside result: {}".format(divition))
    return (divition)
