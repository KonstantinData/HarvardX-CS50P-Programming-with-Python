def main():
    number = get_pin()
    print(number)


def get_pin():
    while True:
        pin = input("PIN: ")
        if pin.isdigit() and len(pin) == 4:
            break
    return pin


main()
