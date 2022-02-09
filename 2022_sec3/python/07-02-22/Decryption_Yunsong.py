# Zhu Yunsong (32)
# 3A3

plainText = ""
condition = True
while condition == True:
    cipherText = input("Enter some cipher text with values in range of 33 to 126: ")
    if cipherText == "":
        print("Please key in some cipher text: ")
    elif cipherText.isdigit() == False:
        print("You can only key in numbers!")
    else: 
        count = 0
        while count < len(cipherText):
            if cipherText[count] == "1": # Checking for 3 digit
                slicedCipherText = int(cipherText[count] + cipherText[count + 1] + cipherText[count + 2])
                if 33 <= slicedCipherText <= 126:
                    plainText += chr(int(cipherText[count] + cipherText[count + 1] + cipherText[count + 2]))
                    count += 3
                else:
                    print("The cipher text you keyed in is out of range! Please re-run the code.")
                    break
            elif cipherText[count] != "1":
                slicedCipherText = int(cipherText[count] + cipherText[count + 1])
                if 33 <= slicedCipherText <= 126:
                    plainText += chr(int(cipherText[count] + cipherText[count + 1]))
                    count += 2
                else:
                    print("The cipher text you keyed in is out of range! Please re-run the code.")
                    break
                
        print(plainText)
        condition = False