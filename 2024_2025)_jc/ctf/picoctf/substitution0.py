charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
sub =     "HPNRSJWLXAOBGUYQDECFZKVMTI0123456789_"
enc = "TD3UN3CSO_4774SV5_4D3_S001_7JJ384LS"

keys = []
dec = ""
flag = ""

for char in enc:
    keys.append(charset[sub.index(char)])

for key in keys:
    flag += charset[charset.index(key)]
    
print(flag)