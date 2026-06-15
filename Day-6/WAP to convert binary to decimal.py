#CODE

# Input a binary number
binary = input("Enter a binary number: ")

decimal = 0
power = 0

# Convert binary to decimal
for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal =", decimal)

#END
