usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    number = int(usernumber)
    if number>=0 and number<6:
        print("Welcome", usernames[number], "user number", number,".")
    else:
        print("the number you want has no name correlated to it")

    if number!=0:
        division = 301 / number
    else:
        division=-1
        print("zeroerror")

    print(f"301 divided by {number} = {division}")

while True:
    inp="a"
    while not inp.isdigit():
        inp = str(input("\nType in a number: "))
    inp=int(inp)
    login_unhandled(inp)
