# Program 5: Reverse a String Using Recursion

def reverse_string(s):
    l = len(s)
    n = ""

    if s == "":
        return n
    else:
        n += s[l - 1] + reverse_string(s[0:l - 1])
        return n


print("Reversed string:", reverse_string("Maanya"))