# Question 1: foo101

def foo101(s):
    if len(s) <= 1:
        return s
    else:
        if s[-1:] == "1" and s[-2:-1] == "0":
            return foo101(s[:len(s) - 2]) + s[-2:-1] + s[-1:]
        elif s[-1:] == "0" and s[-2:-1] == "1":
            return foo101(s[:len(s) - 2]) + s[-1:] + s[-2:-1]
        elif s[-1:] == s[-2:-1]:
            return foo101(s[:len(s) - 2]) + s[-2:]

print(foo101("11010010101"))
print(foo101("0100"))