r1 = [" | | "]
r2 = [" | | "]
r3 = [" | | "]
p = ["_________", r1, "__________", r2, "__________", r3]

print(f"{p[0]}\n{p[1]}\n{p[2]}\n{p[3]}\n{p[4]}\n{p[5]}")

def ask(ans):
    if ans != "o" or "x":
        ans = ask("\nInvalid, please only answer with (O) or (X)"))
    return ans

ask(input("\nWould you like to be O or X?\n").lower())
