#CODE

# Input a number
num = int(input("Enter a number: "))

largest_prime = 1
i = 2

while i <= num:
    if num % i == 0:
        largest_prime = i
        num = num // i
    else:
        i += 1

print("Largest Prime Factor =", largest_prime)

#END