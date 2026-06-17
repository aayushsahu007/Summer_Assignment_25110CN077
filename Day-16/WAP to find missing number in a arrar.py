#CODE

n = int(input("Enter the value of n: "))

arr = []

for i in range(n - 1):
    arr.append(int(input("Enter element: ")))

total = n * (n + 1) // 2
array_sum = sum(arr)

missing = total - array_sum

print("Missing number =", missing)

#END
