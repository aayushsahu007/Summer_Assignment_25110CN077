#CODE

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

arr.sort(reverse=True)

print("Array in Descending Order:")
print(arr)

#END