print("Simple calculator")

a = float(input("first number: "))
b = float(input("second number: "))
op = input("operator (+, -, *, /): ")

if op == "+":
	print(f"Result: {a + b}")
elif op == "-":
	print(f"Result: {a - b}")
elif op == "*":
	print(f"Result: {a * b}")
elif op == "/":
	if b != 0:
		print(f"Result: {a / b}")
	else:
		print("Error: division by zero")
else:
	print("invalid operator")