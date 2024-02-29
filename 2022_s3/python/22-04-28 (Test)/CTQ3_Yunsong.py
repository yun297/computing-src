k = ('Kelly', 'Emma', 'Thomas', 'Alexa', 'Nik', 'Inxs', 'John', 'Cindy')
v = (0, 0, 1, 1, 1, 1, 1, 0)
D1 = {}

# a

for i in range(len(v)):
    if v[i] == 0:
        D1[k[i]] = "Female"
    elif v[i] == 1:
        D1[k[i]] = "Male"

print(D1)

# b

T1 = []
T2 = []

values = D1.values()
keys = D1.keys()

for i in keys:
    if D1[i] == "Female":
        T1.append(i)
    elif D1[i] == "Male":
        T2.append(i)

T1 = tuple(T1)
T2 = tuple(T2)

print(T1)
print(T2)

# c

for i in keys:
    D1[i] = {"Mobile": "0", "Adress": "None"}

D1["Thomas"]["Mobile"] = 82546765

print(D1)
