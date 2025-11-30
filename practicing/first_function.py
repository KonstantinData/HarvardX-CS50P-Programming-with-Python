import os
import json


FILE_PATH = "participants.json"  # match the actual folder name exactly


def main():
    participant = {
        "first_name": input("What's your first name?: "),
        "last_name": input("What's your last name?: "),
        "age": int(input("How old are you?: ")),
        "city": input("Which city do you live in?: "),
    }

    append_participant(FILE_PATH, participant)

    print(greeting(participant))


def append_participant(filename, participant):
    directory = os.path.dirname(filename)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filename, "a", encoding="utf-8") as file:
        file.write(json.dumps(participant))
        file.write("\n")


def greeting(participant):
    return (
        f"Welcome {participant['first_name']} to our study group.\n"
        f"The following data has been saved:\n"
        f"First Name: {participant['first_name']}\n"
        f"Last Name: {participant['last_name']}\n"
        f"Age: {participant['age']}\n"
        f"City: {participant['city']}"
    )


main()
