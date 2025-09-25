def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
num = int(input("Enter a number to find its Fibonacci value: "))

if num < 0:
    print("Please enter a non-negative number.")
else:
    result = fibonacci(num)
    print(f"The Fibonacci number at position {num} is {result}.")

