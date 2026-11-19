# Program 3: Count Digits Using Recursion

def count_digits(n):
    c = 0

    if n == 0:
        return c
    else:
        c += 1 + count_digits(n // 10)
        return c


print("Number of digits:", count_digits(2341))