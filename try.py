usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']
class MummRa(Exception):
    pass

def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    number = int(usernumber)
    if usernumber==5:
        raise MummRa("Bad Bad things will happen")
    try:
        print("Welcome", usernames[number], "user number", number,".")
    except IndexError:
        print("the number you want has no name correlated to it")

    try:
        division = 301 / number
    except ZeroDivisionError:
        division=-1
        print("zeroerror")

    print(f"301 divided by {number} = {division}")


while True:
    try:
        inp = int(input("\nType in a number: "))
    except ValueError:
        print("your input is not accepted")
        inp=-1
    try:
        login_unhandled(inp)
    except MummRa:
        print("not today")