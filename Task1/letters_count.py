str1 = input("Enter a string: ")
sorted_str = sorted(str1)
sorted_string = "".join(sorted_str)
count = {}
for char in str1:
    if char in count:
        count[char] = count[char] + 1
    else:
        count[char] = 1
print(f"Sorted string: {sorted_string}")
print("\nCharacter Counts:")
for char, key in count.items():
    print(f"'{char}' appeared {key} time(s)")

