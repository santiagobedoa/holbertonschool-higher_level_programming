#!/usr/bin/python3


def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print(f"Inside result: {result}")
    except ZeroDivisionError:
        result = None
        print(f"Inside result: {result}")
    finally:
        return result
