def get_guess():
    while True:
        try:
            guess = int(input("Enter a guess: "))
            return guess
        except ValueError:
            print("Only integer numbers allowed")

def main():
    guess = get_guess()
    if guess == 50:
        print("correct")
    else:
        print("incorrect")

main()