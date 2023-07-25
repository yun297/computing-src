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
    s = list(s)

    for i in range(len(s.copy())):
        if int(s[i-1]) < int(s[i]):
            s[i], s[i-1] = s[i-1], s[i]
        
    print(s)    
    
    if complete(s):
        return s
    else:
        return foo101(s)

# def foo101(s):
#     print(s)
    
#     if complete(s):
#         return s
#     else:
#         return foo101(bubbleSort(s))

print(foo101("11010010101"))
print(foo101("0100"))