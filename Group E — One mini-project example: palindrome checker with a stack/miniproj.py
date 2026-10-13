word = input("Enter a word: ")

stack = []

for letter in word:
    stack.append(letter)

backwards = ""
while stack:
    backwards += stack.pop()

if word == backwards:
    print("Palindrome")
else:
    print("Not a palindrome")