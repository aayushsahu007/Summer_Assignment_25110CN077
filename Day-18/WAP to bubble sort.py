#CODE

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input()))

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:")
for num in arr:
    print(num, end=" ")

#END    