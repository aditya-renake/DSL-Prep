books = [2, 0, 5, 2, 1]

print("Average:", sum(books) / len(books))
print("Highest borrow count:", max(books))
print("Lowest borrow count:", min(books))
print("Members who borrowed zero:", books.count(0))

# Find the most common borrow count
most_common = max(set(books), key=books.count)
print("Most common borrow count:", most_common)