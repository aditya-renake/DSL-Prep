class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

expression = "+--a*bc/def"
stack = []
operators = "+-*/"

# Read the expression backwards
for symbol in expression[::-1]:
    node = Node(symbol)

    if symbol in operators:
        node.left = stack.pop()
        node.right = stack.pop()

    stack.append(node)

root = stack.pop()

# Print postorder without recursion
stack = [(root, False)]
answer = []

while stack:
    node, done = stack.pop()

    if done:
        answer.append(node.value)
    else:
        stack.append((node, True))
        if node.right:
            stack.append((node.right, False))
        if node.left:
            stack.append((node.left, False))

print("Postorder:", "".join(answer))