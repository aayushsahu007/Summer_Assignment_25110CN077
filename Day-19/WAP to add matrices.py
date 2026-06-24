#CODE

# Addition of two matrices

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of Matrix 1:")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements of Matrix 2:")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

# Add matrices
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Sum of matrices:")
for row in C:
    print(row)

#END    