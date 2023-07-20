# Question 1: Fibonacci Numbers

def fib(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)

# Question 2: Animals

def is_safe(s):
    if len(s) < 2:
        return True
    else:
        return s[:2] not in "MCDLEMELDCM" and is_safe(s[1:])
    
# Question 3: Palidrome Word

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

print(len("asdfghjkjhgfdsaa "))

# Question 4: Change Cap

def change_cap(s):
    if len(s) == 0:
        return ""
    else:
        if s[0].islower():
            return chr(ord(s[0]) - 32) + change_cap(s[1:])
        else:
            return chr(ord(s[0]) + 32) + change_cap(s[1:])