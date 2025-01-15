def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, u1, v1 = extended_gcd(b % a, a)
        u = v1 - (b // a) * u1
        v = u1
        return gcd, u, v

# Given primes
p = 26513
q = 32321

# Calculate the GCD and coefficients u, v
gcd, u, v = extended_gcd(p, q)

# Output the results
print(f"gcd: {gcd}, u: {u}, v: {v}")

# Determine the lower of u and v
flag = min(u, v)
print(f"Flag: {flag}")
