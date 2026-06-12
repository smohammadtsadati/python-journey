import json

def load_contacts():
	try:
		with open("Contacts.json", "r") as file:
			return json.load(file)
	except FileNotFoundError:
		return []

def save_contacts(contacts):
	with open("contacts.json", "w") as file:
		json.dump(contacts, file, indent=4)

def add_contact():
	contacts = load_contacts()
	name = input("Enter name: ")
	phone = input("Enter phone: ")

	contacts.append({
 		"name": name,
 		"phone": phone
 		})

	save_contacts(contacts)
	print("Contacts saved. ")

def show_contacts():
 	contacts = load_contacts()

 	if len(contacts) == 0:
 		print("No contacts found. ")
 	else:
 		for contact in contacts:
 			print(f"{contact['name']} - {contact['phone']}")

while True:
 	print("\ncontacts JSON App")
 	print("1. Add contact")
 	print("2. Show contacts")
 	print("3. Exit")

 	choise = input("choose: ")

 	if choise == "1":
 		add_contact()
 	elif choise == "2":
 		show_contacts()
 	elif choise == "3":
 		print("Goodbye!")
 		break
 	else:
 		print("Invalid option")