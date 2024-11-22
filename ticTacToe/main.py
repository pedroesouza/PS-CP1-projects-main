r1 = [" | | "]
r2 = [" | | "]
r3 = [" | | "]
p = ["_________", r1, "__________", r2, "__________", r3]

def ask(ans):
    if ans not in ["X", "O"]:
        ans = ask(input("\nInvalid, please only answer with (O) or (X):\n").upper())
    return ans

def ask2(ans1, ans2):
    if ans1 and ans2 not in["1", "2", "3"]:
        ans1 = ask2(input("\nInvalid row selection, please only answer with 1, 2 or, 3:\n"), ans2)
    elif ans1 not in ["1", "2", "3"]:
        ans1 = ask2(input("\nInvalid row selection, please only answer with 1, 2 or, 3:\n"), input("\nInvalid placement on chosen row, please only answer with 1, 2 or 3:\n"))
    elif ans1 not in ["1", "2", "3"]:
        ans3 = ask2(ans1, input("\nInvalid placement on chosen row, please only answer with 1, 2 or 3:\n"))
    return ans1, ans2

choice = ask(input("\nWould you like to be O or X?:\n").upper())

print(f"{p[0]}\n{p[1]}\n{p[2]}\n{p[3]}\n{p[4]}\n{p[5]}")

row, plcmnt = ask2(input(f"\nWhich row would you like to put your {choice} to be? (1, 2, or 3):\n"), input(f"\nWould you like it to be in the 1st, 2nd or 3rd spot in that row?: (1, 2, 3)\n"))