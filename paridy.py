def main():
    x = int(input("What's x ?: "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

"""def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False"""

"""def is_even(n):
    return True if n % 2 == 0 else False"""

def is_even(n):
    return n % 2 == 0 #The boolean operator is returning True/False by itself

main()