class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

# Add three students
first = Node(1, "Asha", 85)
first.next = Node(2, "Ravi", 72)
first.next.next = Node(3, "Mina", 91)

# Display the linked list
current = first
while current:
    print(current.roll, current.name, current.marks)
    current = current.next