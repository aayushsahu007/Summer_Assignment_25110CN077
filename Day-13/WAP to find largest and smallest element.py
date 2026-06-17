#CODE

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

largest = max(arr)
smallest = min(arr)

print("Largest element =", largest)
print("Smallest element =", smallest)

#END