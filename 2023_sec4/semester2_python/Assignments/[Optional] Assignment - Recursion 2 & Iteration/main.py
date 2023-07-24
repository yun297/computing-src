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
    
def bubbleSort(s, i = 0):
    s = list(s)

    if i == len(s):
        return "".join(s)
    elif int(s[i-1]) > int(s[i]):
        s[i], s[i-1] = s[i-1], s[i]
    return bubbleSort(s, i + 1)

def foo101(s):
    if complete(s):
        return s
    else:
        return foo101(bubbleSort(s))

print(foo101("11010010101"))
print(foo101("0100"))