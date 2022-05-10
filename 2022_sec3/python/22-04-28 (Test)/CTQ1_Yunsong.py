num = input("Please enter a number: ")
num3 = (num+num+num)
num2 = (num+num)

try:
    num = int(num)
    num2 = int(num2)
    num3 = int(num3)
except:
    print("Please enter numbers only.")
    exit()

print(num+num2+num3)
