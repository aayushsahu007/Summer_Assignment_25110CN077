#CODE

def armstrong(n):
    temp = n
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** 3
        n = n // 10

    return temp == total

num = int(input("Enter a number: "))

if armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#END    