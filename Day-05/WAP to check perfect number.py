#CODE

# Input a number
num = int(input("Enter a number: "))

sum_divisors = 0

# Find sum of proper divisors
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

# Check perfect number
if sum_divisors == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")

#END    