import json

with open("user.json", "r") as file:
	data = json.load(file)

print("User data: ")
print(data)
print("Name: ", data["name"])
print("Skills: ", data["skills"])