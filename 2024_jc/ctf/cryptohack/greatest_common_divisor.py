def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the function with a = 12, b = 8
print(gcd(12, 8))  # Should output 4

# Now calculate gcd(a, b) for a = 66528, b = 52920
result = gcd(66528, 52920)
print(result)  # Should output the GCD of 66528 and 52920
