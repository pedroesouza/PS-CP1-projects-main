#Pedro Souza, Character creator

import random

stat1 = 0
stat2 = 0
stat3 = 0
stat4 = 0
stat5 = 0
stat6 = 0

d6 = [1, 2, 3, 4, 5, 6]

classes = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "𝘖𝘵𝘩𝘦𝘳"]

species = ["Dragonborn", "Dwarf", "Elf", "Halfling", "Human", "Orc", "Tiefling", "𝘖𝘵𝘩𝘦𝘳"]

stats = {}

print("\033c", end="")

def choose_name():
    playerName = input("What is your characters name?\n")

    return playerName

def choose_species():
    playerSpecies = input(f"\nWhich species would you like to be? (Case sensitive)\nOptions:\n{species}\n")

    if playerSpecies == "Other":
        playerSpecies = input("\nWhat is your Specie's name?\n")

    return playerSpecies

def choose_class():
    playerClass = input(f"\nWhich class would you like to be? (Case sensitive)\nOptions:\n{classes}\n")

    if playerClass == "Other":
        playerClass = input("\nWhat is your Classe's name?\n")

    return playerClass

def choose_stats():
    for i in range(1, 7):
        roll1 = random.choice(d6)
        roll2 = random.choice(d6)
        roll3 = random.choice(d6)
        roll4 = random.choice(d6)

        rolls = [roll1, roll2, roll3, roll4]
        lowestRoll = min(rolls)

        stats["stat{0}".format(i)] = roll1 + roll2 + roll3 + roll4 - lowestRoll

        print(f"\nStat {i}:\nYou rolled a {roll1}, {roll2}, {roll3}, and a {roll4}, since {lowestRoll} was the lowest, it was removed, your stat #{i} is {stats["stat{0}".format(i)]}")

    statsList = list(stats.values())

    srg = input(f"\nYour stats are {statsList}, which one would you like to be your Strength?\n")
    srg = int(srg)
    while srg not in statsList:
        srg = input(f"\nInvalud number! Try again, your stats are {statsList}\n")
        srg = int(srg)
    statsList.pop(statsList.index(srg))

    dex = input(f"\nYour stats are {statsList}, which one would you like to be your Dexterity?\n")
    dex = int(dex)
    while dex not in statsList:
        dex = input(f"\nInvalud number! Try again, your stats are {statsList}\n")
        dex = int(dex)
    statsList.pop(statsList.index(dex))

    con = input(f"\nYour stats are {statsList}, which one would you like to be your Consitution? (Numbers only please)\n")
    con = int(con)
    while con not in statsList:
        con = input(f"\nInvalud number! Try again, your stats are {statsList}\n")
        con = int(con)
    statsList.pop(statsList.index(con))

    inl = input(f"\nYour stats are {statsList}, which one would you like to be your Inteligence?\n")
    inl = int(inl)
    while inl not in statsList:
        inl = input(f"\nInvalud number! Try again, your stats are {statsList}\n")
        inl = int(inl)
    statsList.pop(statsList.index(inl))

    wis = input(f"\nYour stats are {statsList}, which one would you like to be your Wisdom?\n")
    wis = int(wis)
    while wis not in statsList:
        wis = input(f"\nInvalud number! Try again, your stats are {statsList}\n")
        wis = int(wis)
    statsList.pop(statsList.index(wis))

    cha = input(f"\nYour stats are {statsList}, which one would you like to be your Charisma?\n")
    cha = int(cha)
    while cha not in statsList:
        cha = input(f"\nInvalud number! Try again, your stats are {statsList}\n")
        cha = int(cha)
    statsList.pop(statsList.index(cha))

    statsDict = {"str": srg, 
                "dex": dex, 
                "con": con, 
                "int": inl, 
                "wis": wis, 
                "cha": cha
                }
    
    return statsDict

playerName = choose_name()
playerSpecies = choose_species()
playerClass = choose_class()
statsDict = choose_stats()


print(f"\n____________________________________________________________________\n|\n| Species: {playerSpecies}\n| Class: {playerClass}\n| Name: {playerName}\n|\n| Str: {statsDict["str"]}\n|\n| Dex: {statsDict["dex"]}\n|\n| Con: {statsDict["con"]}\n|\n| Int: {statsDict["int"]}\n|\n| Wis: {statsDict["wis"]}\n|\n| Cha: {statsDict["cha"]}\n____________________________________________________________________")

#|                               
#| Species: Elf
#| Class: Bard
#| Name: Jonh Cena
#|
#| Str: 10
#|
#| Dex: 10
#|
#| Con: 10
#|
#| Int: 10
#|
#| Wis: 10
#|                 
#| Cha: 10         
#____________________________________________________________________
