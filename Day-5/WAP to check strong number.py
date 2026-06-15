#CODE

# Input a number
num = int(input("Enter a number: "))

temp = num
sum_fact = 0

# Calculate sum of factorials of digits
while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum_fact += fact
    temp = temp // 10

# Check Strong Number
if sum_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")

#END    