class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Example formula: P AND Q
root = Node("AND")
root.left = Node("P")
root.right = Node("Q")

print("Root operator:", root.value)
print("Left value:", root.left.value)
print("Right value:", root.right.value)