#CODE

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find GCD using Euclidean Algorithm
while b != 0:
    a, b = b, a % b

print("GCD =", a)

#END