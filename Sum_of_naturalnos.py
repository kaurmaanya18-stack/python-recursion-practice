# Program 1: Sum of Natural Numbers Using Recursion

def sum_n(n):
    s = 0

    if n == 1:
        return s + 1
    else:
        s = n + sum_n(n - 1)
        return s


print("Sum:", sum_n(5))