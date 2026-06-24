#CODE

# Program to Check Symmetric Matrix

n = int(input("Enter order of matrix: "))

A = []
print("Enter matrix elements row-wise:")
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

symmetric = True

for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            symmetric = False
            break

if symmetric:
    print("Matrix is Symmetric")
else:
    print("Matrix is Not Symmetric")

#END    