# Name: Zhu Yunsong(32)
# Class: 3A3
# File Name: IOFiles_Yunsong.py

def readA1():
    try:
        A1 = open('2022_sec3/python/17-1-22/A1.txt', 'r')
        print(A1.readline())
        print(A1.readline())
        print(A1.readline())
        A1.close()
    except IOError:
        print('There was an error opening the file!')
        return

def readA2():
    try:
        A2 = open('2022_sec3/python/17-1-22/A2.txt', 'r')
        S1 = A2.readline()
        S2 = A2.readline()
        S3 = A2.readline()
        S4 = A2.readline()
        A2.close()
    except IOError:
        print('There was an error opening the file!')
        return
    
def countLine():
    try:
        A1 = open('2022_sec3/python/17-1-22/A1.txt', 'r')
        A2 = open('2022_sec3/python/17-1-22/A2.txt', 'r')
        
        lineCountA1 = 0
        lineCountA2 = 0
        
        for linesA1 in A1.readlines():
            lineCountA1 += 1
            
        print('Number of lines in A1.txt:', lineCountA1)
        
        for linesA1 in A2.readlines():
            lineCountA2 += 1
            
        print('Number of lines in A2.txt:', lineCountA2)
        
        A1.close()
        A2.close()
    except IOError:
        print('There was an error opening the file!')
        return
    
def fileCreateB1():
    try:
        A1 = open('2022_sec3/python/17-1-22/A1.txt', 'r')
        A2 = open('2022_sec3/python/17-1-22/A2.txt', 'r')
        B1 = open('2022_sec3/python/17-1-22/B1.txt', 'w+')
        B1.write('3A1')
        B1.write('\nNumber of students: 32\n')
        
        i = 0
        
        while i < 22:
            if i == 0:
                tempLine = A2.readline()
                i += 1
            else:
                data = A2.readline()
                B1.write(tempLine)
                i += 1
        
        while i < 34:
            if i == 22:
                tempLine = A2.readline()
                i += 1
            else: 
                tempLine = A2.readline()
                B1.write(tempLine)
                i += 1

        A1.close()
        A2.close()
        B1.close()
    except IOError:
        print('There was an error opening/creating the file!')
        return
    
# readA1()

# readA2()

# countLine()

# fileCreateB1()
