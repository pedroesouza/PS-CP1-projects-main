import random

movePossibilities = ["attack", "defend", "run"]

move = ""

inventory = []

stats = {"Stealth": 1,
         "Strength": 4,
         "Defense": 1,
         "HP": 10
        }

def combat():
    bHP = 15
    while bHP > 0 and stats["HP"] > 0:
        move = input("\nwould you like to ATTACK, DEFEND, or RUN?\n").lower()
        bMove = random.choice(movePossibilities)
        if move == "attack":
            if bMove == "attack":
                bHP -= stats["Strength"]
                stats["HP"] -= 2
                print(f"\nBot health: {bHP}, your health: {stats["HP"]}\n")
            if bMove == "defend":
                bHP -= stats["Strength"]/4
                stats["HP"] -= 0.5
                print(f"\nBot health:{bHP}, your health{stats["HP"]}\n")
            if bMove == "run":
                bHP -= stats["Strength"]
                print(f"\nBot health:{bHP}, your health{stats["HP"]}\n")
        if move == "run":
            if bMove == "attack":
                stats["HP"] -= 2
                print(f"\nBot health:{bHP}, your health{stats["HP"]}\n")
            if bMove == "defend":
                print("\nYou ran away\n")
                break
            if bMove == "run":
                print("\nYou both ran away\n")
                break
        if move == "defend":
            if bMove == "attack":
                stats["HP"] -= 1
                bHP = 1
                print(f"\nBot health:{bHP}, your health{stats["HP"]}\n")
            if bMove == "defend":
                bHP -= 0.5
                stats["HP"] -= 1
                print(f"Bot health:{bHP}, your health{stats["HP"]}")
            if bMove == "run":
                print("\nThe enemy ran away\n")
                break
    if bHP <= 0:
        whatToDo = input("\nYou won, would you like to increase STEALTH, STRENGTH, DEFENSE, or would you like to HEAL?\n").lower()
        if whatToDo == "stength":
            stats["Strength"] += 1
        if whatToDo == "stealth":
            stats["Stealth"] += 1
        if whatToDo == "defense":
            stats["Defense"] += 1
        if whatToDo == "heal":
            stats["HP"] += 2

    if stats["HP"] >= 0:
        print("You lost")
        exit()

def main_area():
    combat()
    print()

def starting_room():
    print("\nYou were wrongully arrested for jay walking, now you must escape prison\n")
    print("\nSuddenly, your cell door  opens, you decide to walk to the main area\n")
    main_area()

starting_room()