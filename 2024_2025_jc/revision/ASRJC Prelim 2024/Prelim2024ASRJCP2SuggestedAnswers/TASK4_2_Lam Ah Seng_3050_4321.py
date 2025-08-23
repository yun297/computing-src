# Task 4.2
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

# main
print(task4_2("Life is hard. Why not make it harder?", "qwertyuiopasdfghjklzxcvbnm"))
# Soyt ol iqkr. Vin fgz dqat oz iqkrtk?
print(task4_2("I love learning H2 Computing in ASR :-)", "qwertyuiopasdfghjklzxcvbnm"))
# O sgct stqkfofu I2 Egdhxzofu of QLK :-)
