# Program 4: Sum of Digits Using Recursion

def sum_digits(n):
    s = 0

    if n == 0:
        return s
    else:
        s += n % 10 + sum_digits(n // 10)
        return s


print("Sum of digits:", sum_digits(32))