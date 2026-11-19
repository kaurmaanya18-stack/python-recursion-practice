# Program 2: Factorial Using Recursion

def factorial(n):
    p = 1

    if n == 0:
        return p
    else:
        p *= n * factorial(n - 1)
        return p


print("Factorial:", factorial(3))