import json

students = [
    {"name": "Taha", "score": 90},
    {"name": "tabasom", "score": 95},
    {"name": "mahdi", "score": 90}
]

with open("students.json", "w") as file:
	json.dump(students, file, indent=4)

print("Students saved.")