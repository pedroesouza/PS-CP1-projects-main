import random
import time

pPoints = 0
bPoints = 0

rps = ["r", "p", "s"]

status = 0

pMove = ""

def ask(answer):
    if answer not in rps:
        pMove = ask(input("r, p, or s?\n").lower())
    return answer

def ask2(answer):
    if answer not in rps:
        pMove = ask(input("r, p, or s?\n").lower())
    return answer

while True:

    print("\033c", end="")

    bMove = random.choice(rps)
    pMove = ask(input("r, p, or s?\n").lower())
        

    time.sleep(0.1)
    print("\nrock...")
    time.sleep(0.5)
    print("paper...")
    time.sleep(0.5)
    print("scissors...")
    time.sleep(0.5)
    print("shoot!")
    time.sleep(0.1)

    print(f"\nYou chose:\n{pMove}")
    time.sleep(0.5)
    print(f"\nBot chose:\n{bMove}") 

    time.sleep(0.5)
    if pMove == "r":
        if bMove == "p":
            status = -1
            print("You lose!")
        elif bMove == "r":
            status = 0
            print("Tie!")
        elif bMove == "s":
            statis = 1
            print("You win!")
    if pMove == "p":
        if bMove == "p":
            status = 0
            print("Tie!")
        elif bMove == "r":
            status = 1
            print("You win!")
        elif bMove == "s":
            statis = -1
            print("You lose!")
    if pMove == "s":
        if bMove == "p":
            status = 1
            print("You win!")
        elif bMove == "r":
            status = -1
            print("You lose!")
        elif bMove == "s":
            statis = 0
            print("Tie!")

    if status == 1:
        pPoints += 1
    elif status == -1:
        bPoints += 1

    time.sleep(0.5)
    print(f"\nYour points:\n{pPoints}")
    time.sleep(0.5)
    print(f"\nBot's points:\n{bPoints}")

    time.sleep(0.5)
    choice = ask2(input("\nGo again (Y/N)\n").lower())
    if choice == "y":
        continue
    else:
        print("Ok! Goodbye!")
        break