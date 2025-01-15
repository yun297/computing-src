enc_flag = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

flag = ""

for i in range(len(enc_flag)):
    enc_flag_ch = enc_flag[i]
    key_ch = key[i]
    
    enc_flag_ord = ord(enc_flag_ch) - ord('A')
    key_ord = ord(key_ch) - ord('A')
    
    flag_ord = (enc_flag_ord - key_ord) % 26
    
    flag += chr(flag_ord + ord('A')) 
    
print(flag)