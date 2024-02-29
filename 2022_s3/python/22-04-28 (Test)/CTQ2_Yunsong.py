str = input("Please enter a word: ")
if not str.isalpha():
    print("Please enter letters only.")

if len(str) % 2 == 0:
    type = 1
    print("Word is even.")
elif len(str) % 2 == 1:
    type = 0
    print("Word is odd.")

if type == 1:
    for i in range(len(str)/2):
        if str[i] == str[-i]:
            print("The word is a palindrome.")
        else:
            print("The word is not a palindrome.")
            exit()
if type == 0:
    for i in range((len(str)-1)/2):
        if str[i] == str[-i]:
            print("The word is a palindrome.")
        else:
            print("The word is not a palindrome.")
            exit()
