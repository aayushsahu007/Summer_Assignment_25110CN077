#CODE

n1 = int(input("Enter size of first array: "))
arr1 = []

for i in range(n1):
    arr1.append(int(input("Enter element: ")))

n2 = int(input("Enter size of second array: "))
arr2 = []

for i in range(n2):
    arr2.append(int(input("Enter element: ")))

union = []

for num in arr1:
    if num not in union:
        union.append(num)

for num in arr2:
    if num not in union:
        union.append(num)

print("Union of arrays:")
print(union)

#END