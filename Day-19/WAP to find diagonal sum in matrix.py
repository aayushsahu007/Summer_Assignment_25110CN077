#CODE

# Find diagonal sum of a square matrix

n = int(input("Enter order of matrix: "))

A = []
print("Enter matrix elements:")
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

diagonal_sum = 0

for i in range(n):
    diagonal_sum += A[i][i]

print("Diagonal Sum =", diagonal_sum)

#END