# Zhu Yunsong (32)
# 3A3

# Times Table
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end=" ")
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
    for j in range(i + 1):
        print("* ", end=" ")
    print("")
print("\n")

# 5x5 Star Upside-down Triangle
for i in range(5):
    for j in range(5 - i):
        print("* ", end=" ")
    print("")
    
# 5x5 Star Inversed Triangle
for i in range(5):
    for j in range(5-i-1):
        print("   ",end="")
    for k in range(i+1):
        print("* ",end=" ")
    print("")