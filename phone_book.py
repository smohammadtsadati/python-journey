contats = {}

while True:
	print("\nPhone Book")
	print("1. Add contact")
	print("3. Find contact")
	print("3. Show all contacts")
	print("4. Exit")

	choice = input("Choose an option: ")

	if choice == "1":
		name = input("Enter name: ")
		phone = input("Enter phone number: ")
		contact[name] = phone
		print("Contact added. ")

	elif choice == "2":
		name = input("Enter name to find: ")
		if name in contacts:
			print(f"{name}: {contacts[name]}")
		else:
			print("Contact not found. ")

	elif choice == "3":
		if len(contacts) == 0:
			print("Phone book is empty. ")
		else:
			for name, phone in contacts.items():
				print(f"{name}: {phone}")

	elif choice == "4":
		print("Goodbye!")
		breaK

	else:
		print("Invalid option. Try again.")