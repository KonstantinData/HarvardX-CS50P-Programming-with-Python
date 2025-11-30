emoticon = "v.v"

def main():
    global emoticon #global allows to midify the global variable emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)

main()
