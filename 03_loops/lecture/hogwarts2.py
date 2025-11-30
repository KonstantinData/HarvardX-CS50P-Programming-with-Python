# Demonstrates iterating over and indexing into a list

"""students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):  # range() expects always an integer
    print(i + 1, students[i])"""

"""students = {
    "hermione": "Griffendor",
    "harry": "Griffendor",
    "ron": "Griffendor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=",")"""

students = [
    {"name": "Hermione", "house": "Griffendor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffendor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffendor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(
        f"{student['name']} from {student['house']} has patronus {student['patronus']}"
    )
