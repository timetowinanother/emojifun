s="1"

def randomletters(s):
    for c in s:
        if c.isalpha(): print(":"+c+":", end="")
        elif c.isdigit(): print(":e"+c+":", end="")
        elif c == " ": print("    ", end="")
        elif c == "!": print(":exclamation:", end="")
        elif c == "?": print(":question:", end="")
        else: print(c, end="")
    print()


def whiteletters(s):
    for c in s:
        if c.isalpha(): print(":alphabet-white-"+c+":", end="")
        elif c.isdigit(): print(":e"+c+":", end="")
        elif c == " ": print("    ", end="")
        elif c == "!": print(":exclamation:", end="")
        elif c == "?": print(":question:", end="")
        else: print(c, end="")
    print()


while s:
    s=input("What characters  would you like to emojify?: ")
    if s == "":
        break
    choice=input("Enter '1' for random letters and '2' for white letters: ")
    if choice == "2": whiteletters(s)
    else: randomletters(s)
