# Q1

from audioop import reverse


def Q1():
    n = int(input("Enter a number: "))
    
    squareNumbers = {}
    
    for i in range(1, n + 1):
        squareNumbers[i] = i * i
        
    print(squareNumbers)
    
# Q2

def Q2():
    D1 = {
        1: 2,
        3: 4,
        4: 3,
        2: 1,
        0: 0
    }
    
    # Sorting by keys
    
    sortedAscendingD1 = {}
    
    for i in sorted(D1.keys()):
        for j, k in D1.items():
            if i == j:
                sortedAscendingD1[j] = k
                
    print(sortedAscendingD1)
    
    print('D1 in ascending order:', sorted(D1.items(), key = lambda x: x[1]))
    
    print('D1 in descending order:', sorted(D1.items(), key = lambda x: x[1], reverse = True))
    
Q2()
    
# Q3

def Q3():
    D1 = {'D': 12,
          'A': 76,
          'F': 8
    }
    
    D2 = {'AA': 22,
          'KK': 67,
          'HH': 56,
          'A': 66
    }

    D3 = {}
    
    for i in D1:
        D3[i] = D1[i]
    
    for i in D2:
        if i not in D3:
            D3[i] = D2[i]
    
    print(D3)
    
# Q4

def Q4():
    D1 = {'a': 100,
          'b': 200,
          'c': 300
    }
    
    D2 = {'a': 300,
          'b': 200,
          'd': 400
    }
    
    D3 = {}
    
    for i in D1:
        D3[i] = D1[i]
        
    for i in D2:
        if i in D3:
            D3[i] += D2[i]
        else:
            D3[i] = D2[i]

    print(D3)