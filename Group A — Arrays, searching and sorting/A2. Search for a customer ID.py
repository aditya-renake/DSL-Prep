ids = [105, 101, 109, 103, 107]
wanted = 103

# Linear search
if wanted in ids:
    print("Linear search: Found")
else:
    print("Linear search: Not found")

# Binary search needs a sorted list
ids.sort()
left = 0
right = len(ids) - 1
found = False

while left <= right:
    middle = (left + right) // 2

    if ids[middle] == wanted:
        found = True
        break
    elif wanted > ids[middle]:
        left = middle + 1
    else:
        right = middle - 1

print("Sorted IDs:", ids)
print("Binary search:", "Found" if found else "Not found")