def triple_and(a, b, c):
    return a and b and c

p1 = input("Enter first value (True or False): ")
p2 = input("Enter second value (True or False): ")
p3 = input("Enter third value (True or False): ")
p1= p1=='True'
p2= p2=='True'
p3= p3=='True'
result = triple_and(p1, p2, p3)
print("Result:", result)
