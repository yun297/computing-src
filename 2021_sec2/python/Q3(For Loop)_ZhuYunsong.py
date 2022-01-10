#Zhu Yunsong
#2i2
#Q3(Forloop)_ZhuYunsong.py

def main():
    x = input("Enter a string: ")
    space = " "
    num=0
    for y in x:
        if y == space:
            continue
        num = num+1
    print (num)

main()