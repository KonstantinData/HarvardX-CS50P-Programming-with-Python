import os
import json
from flask import Flask, render_template, request

app = Flask(__name__)

FILE_PATH = "participants.json"  # Datei in diesem Ordner


def append_participant(filename, participant):
    directory = os.path.dirname(filename)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filename, "a", encoding="utf-8") as file:
        file.write(json.dumps(participant, ensure_ascii=False))
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


@app.route("/", methods=["GET"])
def index():
    # Zeigt nur das Formular
    return render_template("participants_form.html")


@app.route("/submit_participant", methods=["POST"])
def submit_participant():
    # Daten aus dem Formular auslesen
    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()
    age_raw = request.form.get("age", "").strip()
    city = request.form.get("city", "").strip()

    # Age in int umwandeln (einfache Fehlerbehandlung)
    try:
        age = int(age_raw)
    except ValueError:
        age = None

    participant = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "city": city,
    }

    # In Datei schreiben
    append_participant(FILE_PATH, participant)

    # Begrüßungstext erzeugen
    message = greeting(participant)

    # Einfach als Text zurückgeben (später kannst du ein schönes HTML-Template draus machen)
    return f"<pre>{message}</pre>"


if __name__ == "__main__":
    # Lokalen Entwicklungsserver starten
    app.run(debug=True)
