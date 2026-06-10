try:
	a = float(input("Enter first number: "))
	b = float(input("Enter second number: "))
	result = a / b
	print(f"Result: {result}")
except ZeroDivisionError:
	print("You cannot divide by zero")
except ValueError:
	print("Please enter valid numbers")