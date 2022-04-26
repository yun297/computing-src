
Class = {
    "John":81,
    "Bryan Koh":45,
    "Tona":78,
    "Fur":67
    }

Class['Ethan'] = 55

print('Class dictionary sorted:', sorted(Class))

highestKey = Class['John']

for i in Class.values():
    if i > highestKey:
        highestKey = i

print('The highest value is:', highestKey)

lowestItem = ('John', 81)
for i in Class.items():
    if i[1] < lowestItem[1]:
        lowestItem = i
        
print('The lowest item is:', lowestItem)

sum = 0

for i in Class.values():
    sum += i

print('Average of keys:', sum / len(Class))