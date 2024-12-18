import random

movePossibilities = ["attack", "defend", "run"]
jMovePossibilities = ["attack", "defend"]

move = ""
inventory = []
stats = {
    "Stealth": 1,
    "Strength": 4,
    "Defense": 1,
    "HP": 10
}

hasMainAreaFought = False
hasJanitorFought = False

stay = True

def j_combat():
    bHP = 1
    print("You are in combat with the boss")
    while bHP > 0 and stats["HP"] > 0:
        move = input("\nWould you like to ATTACK, DEFEND, or RUN?\n").lower()
        bMove = random.choice(movePossibilities)
        if move == "attack":
            if bMove == "attack":
                bHP -= stats["Strength"]
                stats["HP"] -= 5
            elif bMove == "defend":
                bHP -= stats["Strength"] / (1 + (stats["Defense"] / 5))
                stats["HP"] -= 2
            elif bMove == "run":
                bHP -= stats["Strength"]
            print(f"\nBot health: {bHP}, Your health: {stats['HP']}\n")
        elif move == "run":
            if bMove == "attack":
                stats["HP"] -= 5
            elif bMove == "defend":
                print("\nYOU CAN'T ESCAPE THE JANITOR!!!\n")
            elif bMove == "run":
                print("\nYou both ran away\n")
                break
            print(f"\nBot health: {bHP}, Your health: {stats['HP']}\n")
        elif move == "defend":
            if bMove == "attack":
                stats["HP"] -= 5 / (1 + (stats["Defense"] / 5))
                bHP -= stats["Defense"]
            elif bMove == "defend":
                pass
            elif bMove == "run":
                print("\nThe enemy ran away\n")
                break
            print(f"\nBot health: {bHP}, Your health: {stats['HP']}\n")
    if bHP <= 0:
        print("\nYou won!")
        whatToDo = input("\nWould you like to increase STEALTH, STRENGTH, DEFENSE, or HEAL?\n").lower()
        if whatToDo == "strength":
            stats["Strength"] += 1
        elif whatToDo == "stealth":
            stats["Stealth"] += 1
        elif whatToDo == "defense":
            stats["Defense"] += 1
        elif whatToDo == "heal":
            stats["HP"] += 2
    if stats["HP"] <= 0:
        print("You lost")
        exit()

def c_combat():
    bHP = 5
    print("You are in combat")
    while bHP > 0 and stats["HP"] > 0:
        move = input("\nWould you like to ATTACK, DEFEND, or RUN?\n").lower()
        bMove = random.choice(movePossibilities)
        if move == "attack":
            if bMove == "attack":
                bHP -= stats["Strength"]
                stats["HP"] -= 1
            elif bMove == "defend":
                bHP -= stats["Strength"] / (1 + (stats["Defense"] / 5))
                stats["HP"] -= 0.5
            elif bMove == "run":
                bHP -= stats["Strength"]
            print(f"\nBot health: {bHP}, Your health: {stats['HP']}\n")
        elif move == "run":
            if bMove == "attack":
                stats["HP"] -= 2
            elif bMove == "defend":
                print("\nYou ran away\n")
                break
            elif bMove == "run":
                print("\nYou both ran away\n")
                break
            print(f"\nBot health: {bHP}, Your health: {stats['HP']}\n")
        elif move == "defend":
            if bMove == "attack":
                stats["HP"] -= 2 / (1 + (stats["Defense"] / 5))
                bHP -= stats["Defense"]
            elif bMove == "defend":
                pass
            elif bMove == "run":
                print("\nThe enemy ran away\n")
                break
            print(f"\nBot health: {bHP}, Your health: {stats['HP']}\n")
    if bHP <= 0:
        print("\nYou won!")
        whatToDo = input("\nWould you like to increase STEALTH, STRENGTH, DEFENSE, or HEAL?\n").lower()
        if whatToDo == "strength":
            stats["Strength"] += 1
        elif whatToDo == "stealth":
            stats["Stealth"] += 1
        elif whatToDo == "defense":
            stats["Defense"] += 1
        elif whatToDo == "heal":
            stats["HP"] += 2
    if stats["HP"] <= 0:
        print("You lost")
        exit()

def combat():
    bHP = 15
    print("You are in combat")
    while bHP > 0 and stats["HP"] > 0:
        move = input("\nWould you like to ATTACK, DEFEND, or RUN?\n").lower()
        bMove = random.choice(movePossibilities)
        if move == "attack":
            if bMove == "attack":
                bHP -= stats["Strength"]
                stats["HP"] -= 2
            elif bMove == "defend":
                bHP -= stats["Strength"] / (1 + (stats["Defense"] / 5))
                stats["HP"] -= 0.5
            elif bMove == "run":
                bHP -= stats["Strength"]
            print(f"\nBot health: {bHP}, Your health: {stats['HP']}\n")
        elif move == "run":
            if bMove == "attack":
                stats["HP"] -= 2
            elif bMove == "defend":
                print("\nYou ran away\n")
                break
            elif bMove == "run":
                print("\nYou both ran away\n")
                break
            print(f"\nBot health: {bHP}, Your health: {stats['HP']}\n")
        elif move == "defend":
            if bMove == "attack":
                stats["HP"] -= 2 / (1 + (stats["Defense"] / 5))
                bHP -= stats["Defense"]
            elif bMove == "defend":
                pass
            elif bMove == "run":
                print("\nThe enemy ran away\n")
                break
            print(f"\nBot health: {bHP}, Your health: {stats['HP']}\n")
    if bHP <= 0:
        print("\nYou won!")
        whatToDo = input("\nWould you like to increase STEALTH, STRENGTH, DEFENSE, or HEAL?\n").lower()
        if whatToDo == "strength":
            stats["Strength"] += 1
        elif whatToDo == "stealth":
            stats["Stealth"] += 1
        elif whatToDo == "defense":
            stats["Defense"] += 1
        elif whatToDo == "heal":
            stats["HP"] += 2
    if stats["HP"] <= 0:
        print("You lost")
        exit()

def empty_cell():
    print("\nYou walk into the mysterious room and look right... There is an angry prisoner!")
    combat()
    print("\nYou survived... You decide to walk back to the main area\n")
    main_area()

def hallway_1():
    whereNext = input("\nYou walk through the hall. Would you like to go back to the MAIN AREA or walk to the CAFETERIA?\n").lower()
    if whereNext == "main area":
        main_area()
    elif whereNext == "cafeteria":
        cafeteria()

def janitor_room():
    print(f"inventory: {inventory}")
    whereNext = input("Would you like to use your key to get into the janitors room (Y or N)?").lower()
    if whereNext == "Y":
        print("You unlock the door to see a rope, which you grab, you wall back into hall 2")
        inventory.append("rope")
        hallway_2()
    if whereNext == "N":
        print("Ok... thats kinda dumb, anyways, your back into hallway 2")
        hallway_2()

def hallway_2():
    global hasJanitorFought
    if not hasJanitorFought:
        print("You walk into the hallway to find an angry, incredibly jacked janitor just standing there.")
        j_combat()
        hasJanitorFought = True
        print("\nYou beat him and stolen his key\n")
        inventory.append("key")
    else:
        print("\nYou beat the janitor boss, no one is here\n")
    whereNext = input("\nWould you like to go back to the MAIN AREA or visit the JANITORS ROOM?\n").lower()
    if whereNext == "main area":
        main_area()
    if whereNext == "janitors room":
        janitor_room()

def vent():
    if "rope" in inventory:
        print("The vent is very high up, but then you remember your trusty ROPE, bu using it you climb over the wall and escape though the vents!")
        exit()
    else:
        print("The vent is too high to climb and nothing in your inventory can help with that, you decide to go back to hallway 3")
        hallway_3

def laundry_room():
    whereNext = input("\nYou see a cart! that is your chance to escape... but you will need to be very sneaky, would you like to go back to HALLWAY 4, or TRY ESCAPING\n").lower()
    if whereNext == "hallway 4":
        hallway_4()
    if whereNext == "try escaping":
        if stats["Stealth"] > 9:
            print("\nYou are so sneaky! You managed to escape!!!\n")
            exit()
        else:
            print("You were caught, Game over")
            exit()

def cafeteria():
    print("You walk into the cafeteria to a seemingly infinite amount of weak men that havent eaten in weeks, perfect time to practice fighting!")
    while stay == True:
        c_combat()
        var = input("Do you want to go back to the main area (Y or N)?")
        if var == "y":
            stay == False
        else:
            stay == True

def hallway_4():
    whereNext = input("\nWould you like to go to the LAUNDRY ROOM or back to HALLWAY 3?\n").lower()
    if whereNext == "laundry room":
        laundry_room()
    if whereNext == "hallway 3":
        hallway_3()

def hallway_3():
    whereNext = input("\nYou see a HALLWAY 4, a VENT, and you consider going back to the MAIN AREA, where?").lower()
    if whereNext == "hallway 4":
        hallway_4()
    if whereNext == "main area":
        main_area
    if whereNext == "vent":
        vent()

def main_area():
    global hasMainAreaFought
    if not hasMainAreaFought:
        combat()
        if stats["HP"] > 0:
            hasMainAreaFought = True
    else:
        print("\nThe guard in the main area is defeated\n")
    whereNext = input("\nYou see three hallways (HALLWAY 1, HALLWAY 2, HALLWAY 3) and three empty cells (EMPTY CELL 1, EMPTY CELL 2, EMPTY CELL 3)\n").lower()
    if whereNext == "hallway 1":
        hallway_1()
    elif whereNext == "hallway 2":
        hallway_2()
    elif whereNext == "hallway 3":
        hallway_3()
    elif whereNext in ["empty cell 1", "empty cell 2", "empty cell 3"]:
        empty_cell()

def starting_room():
    print("\nYou were wrongfully arrested for jaywalking. Now you must escape prison\n")
    print("\nSuddenly, your cell door opens. You decide to walk to the main area\n")
    main_area()

print("Combat tutorial: Attacks deal damage to all players, but be careful. If someone defends, the damage will be reduced, and you will take recoil. Defending will temporarily shield you from attacks, but you will still take some damage. You win combat by reducing your opponent's health to 0 or less.\n")
starting_room()
