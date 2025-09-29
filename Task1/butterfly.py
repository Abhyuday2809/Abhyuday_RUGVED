n = int(input("Enter a number (N): "))

for i in range(1, n):
    left = "*" * i
    space = " " * ((2 * (n - i))-1)
    right = "*" * i
    print(left + space + right)

for i in range(n, 0, -1):
    if i==n:
        left = "*" * (i)
        space = " " * ((2 * (n - i))-1)
        right = "*" * (i-1)
        print(left + space + right)
    else:
         left = "*" * i
         space = " " * ((2 * (n - i))-1)
         right = "*" * i
         print(left + space + right)


