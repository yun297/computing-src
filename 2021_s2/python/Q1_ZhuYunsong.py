#Zhu Yunsong 29
#2i2
#Q1_ZhuYunsong.py

def main():
    num = int(input("Enter a number from 1-100: "))
    if(num<1 or num>100):
        print("Please enter a number between 1-100: ")
    elif(num%7==0 and num%5==0):
        print("The number is divisible by 7 and is a multiple of 5.")
    elif(num%7==0):
        print("The number is divisible by 7 but is not a multiple of 5.")
    elif(num%5==0):
        print("The number is not divisible by 7 but is a multiple of 5.")
    else:
        print("Your number is not divisble by 7 and is not a multiple of 5.")

main()
        
