def hex_to_dec(hex):
    hex_table = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    output = 0
        
    for char in range(len(hex)):
        output += hex_table.index(hex[char]) * 16**(len(hex) - char - 1)
        
    return output

print(hex_to_dec("6D"))

def hex_to_dec_ipv6(ipv6):
    ipv6 = ipv6.upper()
    ipv6_list = ipv6.split(":")
    
    dec_list = []
    
    for hextets in ipv6_list:
        dec_list.append(str(hex_to_dec(hextets)))
    
    return ":".join(dec_list)
    
    # return ipv6_list

print(hex_to_dec_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))



