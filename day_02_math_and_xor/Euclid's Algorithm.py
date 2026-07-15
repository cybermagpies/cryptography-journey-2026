def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # 'a' becomes 'b', and 'b' becomes the remainder
    return a

# Test case from the challenge
print(f"Test case gcd(12, 8): {gcd(12, 8)}")

# Challenge case
a = 66528
b = 52920
print(f"Challenge case gcd({a}, {b}): {gcd(a, b)}")