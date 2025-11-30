import os

# Basisordner für SHORTS
base_folder = "05_libraries/shorts/mudules_and_packages"
os.makedirs(base_folder, exist_ok=True)

# Unterordner museum
museum_folder = os.path.join(base_folder, "museum")
os.makedirs(museum_folder, exist_ok=True)

# Dateien aus dem PDF
files = {
    "search.py": """from museum.artwork import get_artwork
from museum.artists import get_artists


def main():
    artist = input("Artist: ")
    artworks = get_artists(query=artist, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")


main()
""",
    "museum/__init__.py": """""",
    "museum/artists.py": """import requests

def get_artists(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search", {"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return [artists["title"] for artists in content["data"]]
""",
    "museum/artwork.py": """import requests

def get_artwork(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return [artwork["title"] for artwork in content["data"]]
""",
}

# Dateien erzeugen
for filename, content in files.items():
    full_path = os.path.join(base_folder, filename)

    # Subdir für museum/ Dateien korrekt erzeugen
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Datei erzeugt: {full_path}")

print("Alle DTO-Shorts wurden erfolgreich erzeugt.")
