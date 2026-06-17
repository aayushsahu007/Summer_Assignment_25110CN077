#CODE

n = int(input("Enter the size of array: "))

arr = []
even = 0
odd = 0

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of Even elements =", even)
print("Number of Odd elements =", odd)

#END