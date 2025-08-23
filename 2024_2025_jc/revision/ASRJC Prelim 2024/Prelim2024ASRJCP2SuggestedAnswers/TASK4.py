import random


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


def task4_2(main_text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""

    # create a dictionary for mapping of chars
    mapping = dict()
    for i in range(26):
        mapping[alphabet[i]] = key[i]

    # encrypt text
    for char in main_text:
        if not char.isalpha():  # non-alphabetical remains unchanged
            encrypted += char
        else:
            if char.islower():
                encrypted += mapping[char]
            else:
                encrypted += mapping[char.lower()].upper()

    return encrypted
            

def task4_3():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = ""
    used_letters = []

    while len(key) < 26:
        # generate random letter
        index = random.randint(0, 25)
        random_letter = alphabet[index]

        # add letter if not used before
        if random_letter not in used_letters:
            key += random_letter
            used_letters.append(random_letter)

    return key


# Main
print(task4_1("Hello everybody!", "key"))
print(task4_1("Hello everybody!", "keyword"))
print(task4_2("Life is hard. Why not make it harder?", "qwertyuiopasdfghjklzxcvbnm"))
print(task4_2("I love learning H2 Computing in ASR :-)", "qwertyuiopasdfghjklzxcvbnm"))
print(task4_3())
