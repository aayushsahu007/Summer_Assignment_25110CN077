#CODE

s = input("Enter a string: ")
ch = input("Enter the character to find frequency: ")

count = 0

for c in s:
    if c == ch:
        count += 1

print("Frequency of", ch, "=", count)

#END