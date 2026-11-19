# Program 8: Calculate Power Using Recursion

def power(a, b):
    p = a

    if b == 1:
        return p
    else:
        p *= power(a, b - 1)
        return p


print("Power:", power(2, 2))