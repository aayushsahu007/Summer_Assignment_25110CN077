#CODE

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

key = int(input("Enter the element to find frequency: "))

count = 0

for num in arr:
    if num == key:
        count += 1

print("Frequency of", key, "=", count)

#END