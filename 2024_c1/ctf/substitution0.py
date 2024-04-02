charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
sub =     "ZGSOCXPQUYHMILERVTBWNAFJDK0123456789_"
enc = "5NG5717N710L_3A0MN710L_357GX9XX"

keys = []
dec = ""
flag = ""

for char in enc:
    keys.append(charset[sub.index(char)])

for key in keys:
    flag += charset[charset.index(key)]
    
print(flag)