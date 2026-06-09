def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		return "Error: division by zero"
	return a / b

def calculate():
	a = float(input("First number: "))
	b = float(input("Second number: "))
	op = input("Operator (+, -, *, /): ")

	if op == "+":
		print(f"Result: {add(a, b)}")
	elif op == "-":
		print(f"Result: {subtract(a, b)}")
	elif op == "*":
		print(f"Result: {multiply(a, b)}")
	elif op == "/":
		print(f"Result: {divide(a, b)}")
	else:
		print("Invalid operator")

calculate()