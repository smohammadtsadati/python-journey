note = input("Enter a note: ")

with open("notes2.txt", "a") as file:
	file.write(note + "\n")

print("Saved with-open. ")