ciphertext = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
key = b"myXORkey"

# Repeat the key to match the ciphertext's length
repeated_key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]

# Decrypt by XORing the ciphertext with the repeated key
flag = bytes(c ^ k for c, k in zip(ciphertext, repeated_key))

print(flag.decode())