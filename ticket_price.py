age = int(input("Enter your age: "))

if age < 12:
	print("Ticket price: 5$")
elif age < 18:
	print("Ticket price: 8$")
elif age < 60:
	print("Ticket price: 10$")
else:
	print("Ticket price: 6$")