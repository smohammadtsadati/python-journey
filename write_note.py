note = input("Enter your note: ")

file = open("notes.txt", "w")
file.write(note)
file.close()

print("Note saved. ")