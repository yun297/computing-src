def xor_string_with_integer(input_string, xor_value):
    # List to hold the resulting characters
    result = []
    
    # Iterate through each character in the input string
    for char in input_string:
        # Convert the character to its Unicode integer
        char_value = ord(char)
        
        # XOR the integer value with the specified integer
        xor_char_value = char_value ^ xor_value
        
        # Convert the XORed value back to a character
        result_char = chr(xor_char_value)
        
        # Append the resulting character to the result list
        result.append(result_char)
    
    # Join the list of characters into a single string
    result_string = ''.join(result)
    
    return result_string

# The given string label
input_label = "label"

# XOR each character of the string with the integer 13
new_string = xor_string_with_integer(input_label, 13)

#Format the result as specified
flag = f"crypto{{{new_string}}}"

print(flag)
