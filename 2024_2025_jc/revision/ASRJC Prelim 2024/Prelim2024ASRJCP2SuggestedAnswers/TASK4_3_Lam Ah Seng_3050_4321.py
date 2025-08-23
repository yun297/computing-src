# Task 4.3
import random

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
	
# main
print(task4_3()) # sample run: wpnadtskxbjvoygzcrufqmheil
