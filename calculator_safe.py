try:
	a = float(input("First number: "))
	b = float(input("Second number: "))
	op = input("Operator (+, -, *, /):")

	if op == "+":
		print(a + b)
	elif op == "-":
		print(a - b)
	elif op == "*":
		print(a * b)
	elif op == "/":
		print(a / b)
	else:
		print("Invalid operator")

except ValueError:
	print("Please enter valid numbers")
except ZeroDivisionError:
	print("You cannot divide by zero")