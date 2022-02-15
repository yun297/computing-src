# Times Table
for i in range(1,11):
    for x in range(1,11):
        print(i*x, end=" ")
    print("")
print("\n")
    
# 5x5 Star Pattern
for i in range (5):
    for i in range (4):
        print("* " , end = " ")
    print("* ")
print("\n")

# 5x5 Star Triangle
for i in range(5):
    for x in range(i + 1):
        print("* ", end=" ")
    print("")
print("\n")

# 5x5 Star Upside-down Triangle
for i in range(5):
    for x in range(5 - i):
        print("* ", end=" ")
    print("")