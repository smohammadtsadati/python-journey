while True:
	try:
		age = int(input("Enter your age: "))
		print(f"Your age is {age}")
		break
	except ValueError:
		print("Please enter a valid number")