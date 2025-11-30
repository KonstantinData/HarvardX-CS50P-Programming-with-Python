"""def main():
    difficulty = input("Difficult or Casual? ")
    Players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if Players == "Multiplayer":
            print("You have chosen a Difficult Multiplayer game.")
            recommend("Poker")
        else:
            print("You have chosen a Difficult Single-player game.")
            recommend("klondike")
    elif difficulty == "Casual":
        if Players == "Multiplayer":
            print("You have chosen a Casual Multiplayer game.")
            recommend("Hearts")
        else:
            print("You have chosen a Casual Single-player game.")
            recommend("Clock")
    else:
        print("Sorry this is not a valid choise")


def recommend(game):
    print("You might like", game)

main()

"""


def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")


def recommend(game):
    print("You might like", game)


main()
