document = ""
undo = []
redo = []

# Add some text
undo.append(document)
document = document + "Hello"
print("Document:", document)

# Undo
redo.append(document)
document = undo.pop()
print("After undo:", document)

# Redo
undo.append(document)
document = redo.pop()
print("After redo:", document)