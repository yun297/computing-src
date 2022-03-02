def encoder():
    key = int(input("Enter a key: "))
    if key >= 0:
        key = key % 94
    else:
        key = key % -94
        
    userText = input("Enter a text to encode: ")
    encodedDecValue = 0
    encodedText = ""
    
    for i in range(len(userText)):
        decValue = ord(userText[i])
        encodedDecValue = decValue + key
        if encodedDecValue > 126:
            encodedDecValue = encodedDecValue - 126 + 31
            encodedText += (chr(encodedDecValue))
        elif encodedDecValue < 32:
            encodedDecValue = 127 - (32 - encodedDecValue)
            encodedText += (chr(encodedDecValue))
        else:
            encodedText += (chr(encodedDecValue))
    print("The encoded text is: " + encodedText)
    
def decoder():
    key = int(input("Enter a key: "))
    if key >= 0:
        key = key % 94
    else:
        key = key % -94
        
    cipherText = input("Enter a cipher text: ")
    decodedDecValue = 0
    decodedText = ""
    
    for i in range(len(cipherText)):
        decValue = ord(cipherText[i])
        decodedDecValue = decValue - key
        if decodedDecValue > 126:
            decodedDecValue = decodedDecValue - 126 + 31
            decodedText += (chr(decodedDecValue))
        elif decodedDecValue < 32:
            decodedDecValue = 127 - (32 - decodedDecValue)
            decodedText += (chr(decodedDecValue))
        else:
            decodedText += (chr(decodedDecValue))
    print("The decoded cipher text is: " + decodedText)
    
while True:
    mode = input("Enter 'e' for encoder, 'd' for decoder, 'q' to quit: ")
    if mode == 'e':
        encoder()
    elif mode == 'd':
        decoder()
    elif mode == 'q':
        exit()
    else:
        print("Please enter one of the above options!")