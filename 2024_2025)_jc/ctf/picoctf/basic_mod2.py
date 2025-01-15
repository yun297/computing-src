charset = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")

numbers = [268, 413, 438, 313, 426, 337, 272, 188, 392, 338, 77, 332, 139, 113, 92, 239, 247, 120, 419, 72, 295, 190, 131]

flag = ""

for num in numbers:
    flag += charset[pow(num % 41, -1, 41) - 1]

print(flag)