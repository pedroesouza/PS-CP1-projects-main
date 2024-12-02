#Pedro Souza, Counting characters


#\/ Importing#
import random
#/\#

#\/ Variable setting.#
letters = ["A", "B", "C", "D", "E"]

gridRow1 = [random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters)]
gridRow2 = [random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters)]
gridRow3 = [random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters)]
gridRow4 = [random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters)]
gridRow5 = [random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters)]
grid = [gridRow1, gridRow2, gridRow3, gridRow4, gridRow5]

aCount = 0
bCount = 0
cCount = 0
dCount = 0
eCount = 0
#/\#

#\/ print, Count and print.#
print(f"{grid[0]}\n{grid[1]}\n{grid[2]}\n{grid[3]}\n{grid[4]}")

for x in grid:
    for y in x:
        if y == "A":
            aCount += 1
        if y == "B":
            bCount += 1
        if y == "C":
            cCount += 1
        if y == "D":
            dCount += 1
        if y == "E":
            eCount += 1
    
print(f"\nA: {aCount}\nB: {bCount}\nC: {cCount}\nD: {dCount}\nE: {eCount}")
#/\#
