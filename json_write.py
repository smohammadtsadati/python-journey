import json

user = {
	"name": "taha",
	"age": 17,
	"skills": ["python", "Git", "problem Solving"]
	}

with open("user.json", "w") as file:
	json.dump(user, file, indent=4)

print("JSON file created.")