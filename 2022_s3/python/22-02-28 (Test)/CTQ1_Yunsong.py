condition = True
count = 0
total = 0
num = 0
product = 1

while True:
    num = input("Enter a number (Press Q to quit): ")
    try:
        num = int(num)
        total += int(num)
        count += 1
        product = product * int(num)
    except:
        
        print("Code exitied!")
        break

if count != 0:
    print("Average =", total/count)
    print("Product =", product)
else:
    print("No number entered!")
