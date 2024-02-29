#Zhu Yunsong 29
#2i2
#Q3_ZhuYunsong.py

def main():
    string = input("Enter a string with 8 charcters, at least 1 number and at least an upper and lower case letter.")
    if(len(string)==8 and string.isalpha() is False and string.isupper() is False and string.islower() is False):
        print("Your string meets all criteria!")
    else:
        print("Your string does not meet 1 or more criteria!")

main()