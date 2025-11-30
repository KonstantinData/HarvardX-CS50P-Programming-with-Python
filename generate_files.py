import os

# Zielordner
folder = "04_exceptions/shorts/handling_exceptions/raising_exceptions"

# Ordner erstellen
os.makedirs(folder, exist_ok=True)

files = {
    "pace0.py": """def main():
    pace = get_pace(miles=26.2, minutes=180)
    print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    return minutes / miles


main()
""",
    "pace1.py": """def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise Exception()
    return minutes / miles


main()
""",
    "pace2.py": """def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError()
    return minutes / miles


main()
""",
    "pace3.py": """def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Minutes must be greater than 0")
    return minutes / miles


main()
""",
}

# Dateien erzeugen
for filename, content in files.items():
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Alle Raising-Exception-Dateien wurden erzeugt.")
