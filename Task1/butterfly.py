n = int(input("Enter a number (N): "))

for i in range(1, n + 1):
    left = "*" * i
    space = " " * (2 * (n - i))
    right = "*" * i
    print(left + space + right)

for i in range(n - 1, 0, -1):
    left = "*" * i
    space = " " * (2 * (n - i))
    right = "*" * i
    print(left + space + right)

