password = ""

while password != "secret123":
	password = input("Enter the password: ")

	if password != "secret123":
		print("Wrong password! Try again.")

print("Access Granted")