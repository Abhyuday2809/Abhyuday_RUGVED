s = input("Enter the string you want to encrypt: ")
key = int(input("Enter the shift key: "))       
new_s = ""
for char in s:
    if char.isupper():
         a = chr((ord(char) - 65 + key) % 26 + 65)
         new_s += a
    elif char.islower():
        a = chr((ord(char) - 97 + key) % 26 + 97)
        new_s += a
    else:
        new_s += char

print(f"Original string:  {s}")
print(f"Encrypted string: {new_s}")