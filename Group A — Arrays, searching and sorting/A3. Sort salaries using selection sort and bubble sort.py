salaries = [45000, 60000, 32000, 75000, 51000]

# Selection sort
a = salaries.copy()
for i in range(len(a)):
    smallest = i
    for j in range(i + 1, len(a)):
        if a[j] < a[smallest]:
            smallest = j
    a[i], a[smallest] = a[smallest], a[i]

print("Selection sort:", a)
print("Top salaries:", a[::-1][:5])

# Bubble sort
b = salaries.copy()
for i in range(len(b)):
    for j in range(len(b) - 1 - i):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]

print("Bubble sort:", b)
print("Top salaries:", b[::-1][:5])