#CODE

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

result = []

for num in arr:
    if num != 0:
        result.append(num)

zero_count = arr.count(0)

for i in range(zero_count):
    result.append(0)

print("Array after moving zeroes to end:")
print(result)

#END