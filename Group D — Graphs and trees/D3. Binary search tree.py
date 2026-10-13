class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = add(root.left, value)
    else:
        root.right = add(root.right, value)
    return root

def show(root):
    if root:
        show(root.left)
        print(root.value, end=" ")
        show(root.right)

def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

root = None
for number in [50, 30, 70, 20, 40]:
    root = add(root, number)

print("Sorted values:", end=" ")
show(root)
print()
print("Search 40:", "Found" if search(root, 40) else "Not found")