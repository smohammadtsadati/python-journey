def add_note():
	note = input("Enter note: ")
	with open("notes.txt", "a") as file:
		file.write(note + "\n")
	print("Note added. ")

def show_notes():
	try:
		with open("notes.txt", "r") as file:
			content = file.read()
			print("\nYour notes: ")
			print(content)
	except FileNotFoundError:
		print("No notes found. ")

while True:
	print("\nNotes App")
	print("1. Add note")
	print("2. show notes")
	print("3, Exit")

	choice = input("Choose: ")

	if choice == "1":
		add_note()
	elif choice == "2":
		show_notes()
	elif choice == "3":
		print("Goodbye! ")
		break
	else:
		print("Invalid option")