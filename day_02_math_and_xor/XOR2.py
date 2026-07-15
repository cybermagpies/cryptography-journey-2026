# The given hex strings
key1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_key3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
encrypted_flag_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# 1. Convert hex strings to bytes
key1 = bytes.fromhex(key1_hex)
key2_key3 = bytes.fromhex(key2_key3_hex)
encrypted_flag = bytes.fromhex(encrypted_flag_hex)

# 2. XOR the bytes together
# zip() lets us pair up the bytes from each variable and XOR them one by one
flag_bytes = bytes(a ^ b ^ c for a, b, c in zip(key1, key2_key3, encrypted_flag))

# 3. Decode bytes to a string and print
print(flag_bytes.decode())