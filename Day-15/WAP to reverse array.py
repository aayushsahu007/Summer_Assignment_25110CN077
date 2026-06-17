#CODE

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Reversed array:")

for i in range(n - 1, -1, -1):
    print(arr[i], end=" ")

#END    