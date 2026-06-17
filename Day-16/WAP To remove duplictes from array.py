#CODE

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Array after removing duplicates:")
print(unique)

#END