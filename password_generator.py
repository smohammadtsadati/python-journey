import random
import string

try:
	length = int(input("Enter password length: "))

	if length <= 0:
		print("Please enter a number greater than 0")
	else:
		letters = string.ascii_letters
		numbers = string.digits
		symbols = string.punctuation

		all_chars = letters + numbers + symbols

		password = ""

		for i in range(length):
			password += random.choice(all_chars)

		print("Generated password: ", password)

except ValueError:
	print("Please enter a valid number")