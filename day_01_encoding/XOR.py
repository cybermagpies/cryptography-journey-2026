label = "label"

result = ""

for char in label:
    result += chr(ord(char) ^ 13)

print(f"crypto{{{result}}}")