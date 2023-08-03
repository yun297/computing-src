# Question 1: foo101
def complete(s):
    count = 0
    for char in s:
        if int(char) > count:
            count = int(char)
        elif int(char) < count:
            return False
    else:
        return True
    
def foo101(s):
    if len(s) == 0:
        return ""
    elif s[0] == "0":
        return s[0] + foo101(s[1:])
    elif s[0] == "1":
        return foo101(s[1:]) + s[0]

# print(foo101("11010010101"))
# print(foo101("0100"))

# Question 2: foo123

def foo123(s, x = 0, y = 0, z = 0):
    if len(s) == 0:
        return "1"*x + "2"*y + "3"*z
    elif s[0] == "1":
        return foo123(s[1:], x+1, y, z)
    elif s[0] == "2":
        return foo123(s[1:], x, y+1, z)
    elif s[0] == "3":
        return foo123(s[1:], x, y, z+1)

# foo123("13233112331231332")

def fooABC(s):
    check = 0
    for char in s:
        if ord(char) < check:
            break
        else:
            check = ord(char)
    else:
        return s
    
    s = list(s)
    
    for i in range(1, len(s)):
        if ord(s[i]) < ord(s[i-1]):
            s[i], s[i-1] = s[i-1], s[i]
    
    return fooABC("".join(s))

print(fooABC("imhimhimhihihm"))

def deep_contains(obj, tup):
    
    if isinstance(obj, tuple):
        for value in obj:
            if value is tup:
                return True
            else:
                return deep_contains(value, tup)
        else:
            return False
    
# do not touch. needed for public test cases
x = (1,2)
a = ((1,2), ((3,4), x), (5,6))