
og_str = input("Enter your string: ")
part_len_str = input("Enter the length of each part (e.g., 4): ")
part_len = int(part_len_str)
str_len = len(og_str)
if str_len % part_len != 0:
    print("\nError: The string cannot be divided into equal parts of that length.")

else:
    first = og_str[0 : part_len]
    parts_match= True
    parts = []
    for i in range(0, str_len, part_len):
        part1 = og_str[i : i + part_len]
        parts.append(part1)
        if part1 != first:
            parts_match = False
            break
        
            

    if parts_match:
        print("\nSuccess! All parts are the same:")
        print(parts)
    else:
        print("\nError: The string can be divided, but the parts are not the same.")

