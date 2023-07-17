# Question 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
    
def sum_odd_factorials(n):
    # Returns the sum of factorials of odd numbers 
    # that are less than or equal to n.
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        n -= 1
        
    return factorial(n) + sum_odd_factorials(n - 2)

# print(sum_odd_factorials(0))
# print(sum_odd_factorials(3))
# print(sum_odd_factorials(6))

# Question 2

def collatz_distance(n, steps = 0):
    if n == 1:
        return steps
    elif n % 2 == 0:
        return collatz_distance(n / 2, steps + 1)
    elif n % 2 == 1:
        return collatz_distance(3 * n + 1, steps + 1)
    
# print(collatz_distance(1))
# print(collatz_distance(4))
# print(collatz_distance(27))

# Question 3

def replace_digit(n, d, r):
    if n == 0:
        return 0
    elif n % 10 == d:
        return replace_digit(n // 10, d, r) * 10 + r # Replace the digit
    else:
        return replace_digit(n // 10, d, r) * 10 + n % 10 # Keep the digit
    
# print(replace_digit(123, 2, 0))
# print(replace_digit(1234, 1, 0))
# print(replace_digit(122234, 2, 5))

# Question 4

def powers_of_two(power, exponent = 0): # Iterative function
    while power % 2 == 0:
        power /= 2
        exponent += 1
    return exponent

print(powers_of_two(8))

# Question 5

def powers_of_two(power, exponent = 0): # Recursive function
    if power % 2 == 0:
        return powers_of_two(power / 2, exponent + 1)
    else:
        return exponent