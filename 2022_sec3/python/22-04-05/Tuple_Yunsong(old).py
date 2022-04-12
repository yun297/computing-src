T1 = (78, 45, 89, 66, 90, 50, 89, 89, 90) 
T2 = (50, 45, 90, 66)

# a)

def a():    
    sum = 0
    average = 0

    for i in T1:
        sum += i
    for i in T2:
        sum += i
    average = sum/(len(T1)/len(T2))

    print('Average: ', average)

# b)

def b():
    largestNum1 = 0
    largestNum2 = 0

    for i in T1:
        if i > largestNum1:
            largestNum1 = i
    for i in T1:
        if i > largestNum2 and i < largestNum1:
            largestNum2 = i

    print('Largest Number:', largestNum1)
    print('Second Largest Number:', largestNum2)
    
# c)

def c():
    smallestNum1 = 100
    smallestNum2 = 100

    for i in T1:
        if i < smallestNum1:
            smallestNum1 = i
    for i in T1:
        if i < smallestNum2 and i > smallestNum1:
            smallestNum2 = i
    
    print('Smallest Number:', smallestNum1)
    print('Second Smallest Number:', smallestNum2)
    
# d)

def d():
    try:
        userNum = int(input('Enter a number: '))
    except:
        print('Invalid input')
        exit()
    
    if userNum in T1:
        print('Number is in the list.')
    else:
        print('Number is not in the list.')
    
# e)

def e():
    # L1 = list(T1)
    # L2 = []
    
    # for i in L1:
    #     if L1.count(i)>1:
    #         L2.append(i)
    
    # L2 = set(L2)
    
    # print('Duplicate numbers: ', end = '')
    
    # for i in L2:
    #     print(i, end = ' ')
        
    print("Duplicated numbers: ", end = '')
    [print(j, end=' ') for j in set([i for i in T1 if T1.count(i) > 1])]
        
# f)

def f():
    L1 = [i for i in T1 if i < 74]
    L2 = [j for j in T1 if j >= 74]
    
    print('L1:', L1)
    print('L2:', L2)
    
# g)

def g():
    print(T1[::-1])
    
# h)

def h():
    print('Numbers that are in both T1 and T2: ', end = '')
    print([i for i in T1 if i in T2])
    
# i)

def i():
    # global T1 # For some reason T1 is not reocgnised in the function so I have to use either a new local variable iT1 or global T1
    
    L1 = list(T1)
    L1.insert(4, 100)
    iT1 = tuple(L1)
    
    print(iT1)
    
def j():
    # global T1 # For some reason T1 is not reocgnised in the function so I have to use either a new local variable jT1 or global T1
    
    L1 = list(T1)
    L1.pop(-2)
    jT1 = tuple(L1)
    
    print(jT1)