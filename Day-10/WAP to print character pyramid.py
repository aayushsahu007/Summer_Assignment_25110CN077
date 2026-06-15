#CODE

rows = int(input("enter number:"))

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")

    # Print increasing characters
    for j in range(i):
        print(chr(65 + j), end="")

    # Print decreasing characters
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")

    print()