charset = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")

numbers = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]

flag = ""

for num in numbers:
    flag += charset[num % 37]
    
print(flag)