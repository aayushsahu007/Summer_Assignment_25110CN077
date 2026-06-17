#CODE

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

last = arr[n - 1]

for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]

arr[0] = last

print("Array after right rotation:")
for i in arr:
    print(i, end=" ")

#END    