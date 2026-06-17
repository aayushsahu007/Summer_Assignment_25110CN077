#CODE

# Input nth term
n = int(input("Enter the value of n: "))

a, b = 0, 1

for i in range(n - 1):
    a, b = b, a + b

print("The", n, "th Fibonacci term is", a)

#END