#CODE

# Transpose of a matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix elements:")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

# Transpose matrix
T = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(A[i][j])
    T.append(row)

print("Transpose of matrix:")
for row in T:
    print(row)

#END    