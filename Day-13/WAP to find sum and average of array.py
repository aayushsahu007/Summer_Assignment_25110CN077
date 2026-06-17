#CODE

n = int(input("Enter the size of array: "))

arr = []
total = 0

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)
    total += element

average = total / n

print("Sum =", total)
print("Average =", average)

#END