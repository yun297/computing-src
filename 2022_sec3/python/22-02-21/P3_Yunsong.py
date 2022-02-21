# Zhu Yunsong (32)
# 3A3

# Question 1:

from cgitb import small


def Q1():
    year = input("Enter a year: ")
    try:
        if year == "":
            print("Please key in a year!")
        else:
            year = int(year)
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                print("The year is a leap year.")
            else:
                print("The year is not a leap year.")
    except ValueError:
        print("You can only key in numbers!")

# Question 2:

def Q2():
    num = int(input("Enter a number: "))

    reverseNum = 0

    while num > 0:
        remVal = num % 10
        reverseNum = reverseNum * 10 + remVal
        num = num // 10
    
    print(reverseNum)

# Question 3:

def Q3():
    num = int(input("Enter a number: "))
    
    try:
        num = int(num)
    except:
        print("You can only key in numbers!")
        exit()
    
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    print(factorial)
    
# Question 4:

def Q4():
    goal = int(input("Enter the goal: "))
    smallBricks = int(input("Enter the number of small bricks: "))
    largeBricks = int(input("Enter the number of large bricks: "))
    
    largeBricks += (smallBricks // 5)
    largeFromSmall = smallBricks // 5
    smallBricks -= largeFromSmall * 5
    
    if goal // 5 <= largeBricks and goal % 5 <= smallBricks:
        print("You can make it!")
    else:
        print("You can't make it!")