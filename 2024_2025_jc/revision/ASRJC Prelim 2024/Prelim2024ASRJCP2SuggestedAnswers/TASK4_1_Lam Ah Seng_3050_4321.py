# Task 4.1
def task4_1(main_text, keyword):
    encrypted = ""
    prev_encrypted = ""  # store previously encrypted char
    keyword = keyword.lower()
    key_index = 0  # track current position in keyword

    for i in range(len(main_text)):
        char = main_text[i]
        if char.isalpha():
            if key_index < len(keyword):  # use keyword char
                key_char = keyword[key_index]
            else:  # use prev encrypted char
                key_char = prev_encrypted
                
            # calc shift
            shift = ord(key_char) - ord("a")

            # get new ascii value within bounds
            new_ascii = ord(char) + shift
            if (char.isupper() and new_ascii > ord("Z")) \
               or (char.islower() and new_ascii > ord("z")):
                new_ascii -= 26
                
            encrypted += chr(new_ascii)
            prev_encrypted = chr(new_ascii)
            key_index += 1
            
        else:  # non-alphabet
            encrypted += char
            
    return encrypted


# main
print(task4_1("Hello everybody!", "key"))       # Rijui mhlcabpsq!
print(task4_1("Hello everybody!", "keyword"))   # Rijhc vyctrsgjh!
