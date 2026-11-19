# Program 6: Count Character Occurrences Using Recursion

def count_char(s, ch):
    sch = 0

    if s == "":
        return sch
    else:
        if ch == s[0]:
            sch += 1 + count_char(s[1:], ch)
            return sch
        else:
            sch += 0 + count_char(s[1:], ch)
            return sch


print("Occurrences:", count_char("Maanya", "a"))