# Step 1

K1 = []
V1 = []

# Step 2

for i in range(1,4):
    K1.append(i)

# Step 3
    
V1.extend(['OCBC', 'UOB', 'DBS'])

# Step 4

tempList = []

tempList = K1

K1 = V1

V1 = tempList

print(K1)
print(V1)