def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Invalid input for difficulty")
        return

    players = input("Multiplayer or Singleplayer? ")
    if not (players == "Multiplayer" or players == "Singleplayer"):
        print("Invalid input for players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Singleplayer":
        recommend("Hearts")
    elif difficulty == "Casual" and players == "Singleplayer":
        recommend("Klondike")
    else:
        print("Invalid input")


def recommend(game):
    print("You might like", game)


main()
