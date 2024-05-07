s=input("What do you want to emojify?: ")

for c in s:
        if c.isdigit() or c.isalpha(): print(":"+c+":", end="")
        elif c == " ": print("    ", end="")
        elif c == "!": print(":exclamation:", end="")
        elif c == "?": print(":question:", end="")
        else: print(c, end="")

print()
