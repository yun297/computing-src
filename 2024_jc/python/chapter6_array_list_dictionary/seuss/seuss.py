seuss = open("2024_c1\python\chapter6_array_list_dictionary\seuss\seuss.txt", "r")
wordlist = {}
wordlist_sorted = {}

for line in seuss:
    line = line.strip()
    
    for i in [",", "?", "!", "."]:
        line = line.replace(i, " ")
        
    for word in line.split(" "):
        if word.lower() not in wordlist and word != "":
            wordlist[word.lower()] = 1
        elif word.lower() != "":
            wordlist[word.lower()] += 1

seuss.close()

def get_value(item):
    return item[1]

wordlist_sorted = dict(sorted(wordlist.items(), key = get_value, reverse = True))
sorted()

print(wordlist_sorted)