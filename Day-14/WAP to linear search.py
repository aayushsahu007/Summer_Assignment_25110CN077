#CODE

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

key = int(input("Enter element to search: "))

found = False

for i in range(n):
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")

#END    