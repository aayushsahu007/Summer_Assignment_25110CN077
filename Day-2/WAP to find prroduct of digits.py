#CODE

# Input a number
num = int(input("Enter a number: "))

product = 1

# Calculate product of digits
while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10

print("Product of digits =", product)

#END