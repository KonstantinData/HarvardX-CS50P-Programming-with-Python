name = input ("Whats's your name? ")

Griffindor = ["Harry", "Hermione", "Ron"]

match name:
    case n if n in Griffindor:
        print("Gryffindor")
    case "Drago":
        print("Slytherin")
    case _:
        print("Who?")