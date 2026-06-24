#CODE

# Matrix Multiplication in Python

r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

A = []


r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

A = []
print("Enter elements of first matrix:")
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    A.append(row)

B = []
print("Enter elements of second matrix:")
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input()))
    B.append(row)

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    result = [[0 for j in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix:")
    for row in result:
        print(row)

#END        