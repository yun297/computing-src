# Question 1: Factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return(n * factorial(n - 1))

# Question 2: Sum of Positive Even Numbers

def sum_of_n_even_numbers(n):
    if n == 1:
        return 2
    current_even = 2 * n
    return current_even + sum_of_n_even_numbers(n - 1)

# Question 3: Sum of First n Odd Numbers

def sum_odd_n(n):
    if n == 1:
        return 1
    current_odd = 2 * n - 1
    return current_odd + sum_odd_n(n - 1)

# Question 4: Sum of First n Squares

def sum_n_squares(n):
    if n == 1:
        return 1
    current_square = n**2
    return current_square + sum_n_squares(n - 1)

# Qyestion 5

def foo(n):
    if n == 0:
        return 0
    else:
        return 2 * n + foo(n - 1)
    
# print(foo(5))

# Question 6

def bar(n):
    if n < 3:
        return n + 1
    else:
        return bar(n - 3) + bar(n - 2) + bar(n - 1)
    
# print(bar(4))

# Question 7

def hike(current_altitude):
    if current_altitude > 40:
        return 0
    else:
        return 1 + slide(current_altitude + 11)

def slide(current_altitude):
    if current_altitude > 40:
        return 0
    else:
        return hike(current_altitude - 3)

n = hike(0)

# print(n)