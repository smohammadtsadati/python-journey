def celsius_to_fahrenheit(c):
	return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
	return (f - 32) * 5/9

while True:
	print("\nTemperature Converter")
	print("1. Celsius To Farhenheit")
	print("2. Farhenheit To Celsius")
	print("3. Exit")

	choice = input("Choose: ")

	if choice == "1":
		c = float(input("Enter Celsius: "))
		print(f"Result: {celsius_to_fahrenheit(c):.1f}F")
	elif choice == "2":
		f = float(input("Enter Farhenheit: "))
		print(f"Result: {fahrenheit_to_celsius(f):.1f}C")
	elif choice == "3":
		break
	else:
		print("Invalid option")