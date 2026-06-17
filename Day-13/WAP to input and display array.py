#CODE

# Input array elements
n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

# Display array elements
print("Array elements are:")
for i in arr:
    print(i, end=" ")

#END    