file = open("notes.txt", "r")
content = file.read()
file.close()

print("Your notes: ")
print(content)