#CODE

# Input a number
num = int(input("Enter a number: "))

temp = num
sum = 0
digits = len(str(num))

# Calculate sum of digits raised to the power of number of digits
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp = temp // 10

# Check Armstrong number
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")

#END    