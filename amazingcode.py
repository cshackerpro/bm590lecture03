def amazingcode(num1, num2):
    if !isinstance(num1, int):
        print "Type Error: first arg is not an int"
        return
    if !isinstance(num2, int):
        print "Type Error: second arg is not an int"
        return
    summation = num1 + num2
    if (summation < 0):
        return 0
    else: 
        return summation

