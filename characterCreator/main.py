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
    name = input("What is your characters name?\n")

def choose_species():
    playerSpecies = input(f"\nWhich species would you like to be(case sensitive)?\nOptions:\n{species}\n")

    if playerSpecies == "Other":
        playerSpecies = input("\nWhat is your Specie's name?\n")

def choose_class():
    playerClass = input(f"\nWhich class would you like to be(case sensitive)?\nOptions:\n{classes}\n")

    if playerClass == "Other":
        playerClass = input("\nWhat is your Classe's name?\n")

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

choose_name()
choose_species()
choose_class()
choose_stats()