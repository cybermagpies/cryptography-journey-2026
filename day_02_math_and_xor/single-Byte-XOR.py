hex_ciphertext = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Convert the hex string back to bytes
ciphertext_bytes = bytes.fromhex(hex_ciphertext)

# Brute-force all 256 possible single-byte keys
for key in range(256):
    # XOR each byte in the ciphertext with the current key candidate
    decrypted = bytes(b ^ key for b in ciphertext_bytes)
    
    # Check if we successfully decrypted the flag format
    if b"crypto{" in decrypted:
        print(f"[+] Found Key: {key} (Hex: {hex(key)})")
        print(f"[+] Decrypted Flag: {decrypted.decode()}")
        break