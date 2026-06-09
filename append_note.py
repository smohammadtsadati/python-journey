note = input("Enter another note: ")

file = open("notes.txt", "a")
file.write(note + "\n")
file.close()

print("Note added. ")