p = 29
candidates = [14, 6, 11]

# We will store the squares here
squares = {}

for a in range(1, p):
    square = (a * a) % p
    squares[square] = a

# Check which candidate is a perfect square (quadratic residue)
for x in candidates:
    if x in squares:
        # Since we found a square root 'a', the other root is p - a (which is equivalent to -a)
        root1 = squares[x]
        root2 = p - root1
        print(f"Quadratic Residue: {x}")
        print(f"Roots: {root1} and {root2}")
        print(f"Smaller root (Flag): {min(root1, root2)}")