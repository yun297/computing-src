seuss = open("2024_c1\python\chapter6_array_list_dictionary\seuss\seuss.txt", "r")
wordlist = {}

for line in seuss:
    line = line.strip()
    
    for i in [",", "?", "!", "-", "."]:
        line = line.replace(i, " ")
        
    for word in line.split(" "):
        if word not in wordlist and word != "":
            wordlist[word] = 1
        elif word != "":
            wordlist[word] += 1

print(wordlist)

seuss.close()