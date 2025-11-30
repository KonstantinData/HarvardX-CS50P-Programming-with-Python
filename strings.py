SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "jimmi Neutron ",
    "the Proud family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print("\n".join(f"{i+1}. {show}" for i, show in enumerate(cleaned_shows)))

main()
