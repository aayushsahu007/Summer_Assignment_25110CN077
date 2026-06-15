#CODE

# Input base and exponent
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

result = 1

# Calculate x^n
for i in range(n):
    result *= x

print("Result =", result)

#END