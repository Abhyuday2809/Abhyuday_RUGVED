str1 = input("Enter a string to sort: ")
char_list = list(str1)
ste_len = len(char_list)
for i in range(ste_len):
    min_index = i
    for j in range(i + 1, ste_len):
        if char_list[j] < char_list[min_index]:
            min_index = j
    temp = char_list[i]
    char_list[i] = char_list[min_index]
    char_list[min_index] = temp
sorted_result = "".join(char_list)
print(f"Entered string: {str1}")
print(f"Sorted string:   {sorted_result}")

