#CODE

# Input a number
num = int(input("Enter a number: "))

reverse = 0

# Reverse the number
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)

#END