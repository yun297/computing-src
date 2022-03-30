# Question 1

def Q1():
    Q1L1 = []
    for i in range(5):
        Q1L1.append(input("Enter a string 5 times: "))
    print(Q1L1)

# Question 2

def Q2():
    Q2L1 = ['One', 'True', 'Vice', 'Well']
    Q2L2 = ['People', 'Colours', 'Versa ', '-being', 'Summation']
    Q2L3 = []

    sizeMin = min(len(Q2L1), len(Q2L2))
    
    tempVar = ''

    for i in range(sizeMin):
        tempVar = Q2L1[i] + Q2L2[i]
        Q2L3.append(tempVar)

    if len(Q2L1) > len(Q2L2):
        for j in range(i + 1, len(Q2L1)):
            Q2L3.append(Q2L1[j])
    elif len(Q2L2) > len(Q2L1):
        for j in range(i + 1, len(Q2L2)):
            Q2L3.append(Q2L2[j])
        
    print(Q2L3)

# Question 3

def Q3():
    Q3L4 = ['A', 'M', '121', 'M', 'N', 'A', '121']
    
    tempList = []
    for i in Q3L4:
        if i not in tempList:
            tempList.append(i)
    
    Q3L4 = tempList
    print(Q3L4)
    
# Question 4

def Q4():
    Q4L1 = [
        [1,2],
        [3,4],
        [5,6],
        [7,8]
    ]
    
    # Sum of all numbers
    
    sum = 0
        
    for i in range(len(Q4L1)):
        for j in range(len(Q4L1[i])):
            sum += Q4L1[i][j]
            
    print("Sum: ", sum)
    
    # The pair with the biggest and smallest sum of both numbers
    
    Q4L1.sort()
    print(Q4L1[0])
    print(Q4L1[-1])
    
    ## Defining variables
    
    # tempPair = []
    # tempSum = 0
    # minPair = []
    # minSum = 16
    # maxPair = []
    # maxSum = 0
    
    # ## Finding the pair with the smallest sum of both numbers
    
    # for i in range(len(Q4L1)):
    #     tempPair = Q4L1[i]
    #     tempSum = Q4L1[i][0] + Q4L1[i][1]
    #     if tempSum < minSum:
    #         minPair = tempPair
    #         minSum = tempSum
    #     else:
    #         continue
        
    # print("Min Pair: ", minPair, "Sum: ", minSum)
    
    # ## Finding the pair with the biggest sum of both numbers
    
    # for i in range(len(Q4L1)):
    #     tempPair = Q4L1[i]
    #     tempSum = Q4L1[i][0] + Q4L1[i][1]
    #     if tempSum > maxSum:
    #         maxPair = tempPair
    #         maxSum = tempSum
    #     else:
    #         continue
    
    # print("Max Pair: ", maxPair, "Sum: ", maxSum)
    
Q4()