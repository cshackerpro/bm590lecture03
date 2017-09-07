def amazingcode(num1, num2):
    if (type(num1) != int):
        raise ValueError('Type Error: first arg is not an int')
    if (type(num2) != int):
        raise ValueError('Type Error: second arg is not an int')
    summation = num1 + num2
    if (summation < 0):
        return 0
    else: 
        return summation

