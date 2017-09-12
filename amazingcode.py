import pytest

def amazingcode(num1, num2):
    if (type(num1) != int):
        raise ValueError('Type Error: first arg is not an int')
    if (type(num2) != int):
        raise ValueError('Type Error: second arg is not an int')
    sum_num = num1 + num2
    if (sum_num < 0):
        return 0
    else:
        return sum_num
