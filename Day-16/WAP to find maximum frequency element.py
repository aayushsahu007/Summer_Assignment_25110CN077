#CODE

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

max_count = 0
max_element = arr[0]

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1

    if count > max_count:
        max_count = count
        max_element = arr[i]

print("Maximum Frequency Element =", max_element)
print("Frequency =", max_count)

#END