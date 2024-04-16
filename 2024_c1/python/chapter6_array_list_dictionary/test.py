lst = [1, 2, 3, 4, 5]
lst2 = lst

lst.append(6)

print(lst)
print(lst2)

print(lst is lst2)

lst3 = lst.copy()

print(lst3)
print(lst3 is lst)