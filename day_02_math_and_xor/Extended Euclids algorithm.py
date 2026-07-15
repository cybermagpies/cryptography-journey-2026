def extended_gcd(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    
    gcd, u1, v1 = extended_gcd(b % a, a)
    
    # Update u and v using results of recursive call
    u = v1 - (b // a) * u1
    v = u1
    
    return gcd, u, v

p = 26513
q = 32321

gcd_val, u, v = extended_gcd(p, q)

print(f"gcd({p}, {q}) = {gcd_val}")
print(f"u = {u}")
print(f"v = {v}")
print(f"Verification: {p} * ({u}) + {q} * ({v}) = {p*u + q*v}")
print(f"Lower of the two: {min(u, v)}")