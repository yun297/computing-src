def interest(n):
    if n <= 1:
        return 500 * 1.006
    else:
        return 500 * 1.006 + interest(n - 1) * 1.006
    
print(interest(3))

balance = 0
n = 3
for i in range (n):
    balance += 500
    balance += balance * 0.006
    # print(balance)
    
print(balance)

