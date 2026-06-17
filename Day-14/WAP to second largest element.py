#CODE

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

arr.sort()

print("Second Largest Element =", arr[-2])

#END