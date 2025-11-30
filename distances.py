distances = {
    "Voyager 1": 163,
    "Voyager 2": 129,
    "Pioneer 10": 122,
    "Pioneer 11": 101,
    "New Horizons": 50
}


"""def main():
    for name in distances.keys():
        print(f"{name}: {distances[name]} AU from Earth")


main()"""

def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")
def convert(au):
    return au * 149597870700

main()