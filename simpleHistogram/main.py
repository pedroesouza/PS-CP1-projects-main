#Pedro E Souza, Histogram
numList = []

amount = int(input("\nHow man lines do you want?\n"))

for iAmount in range(1, amount + 1):
    numList.append(int(input(f"\nWhat do you want number {iAmount} to be in your list?\n")))

print("\n")

for iLength in range(0, len(numList)):
    print(f"{iLength}: ", end = "")
    for iAsterisk in range(numList[iLength]):
        print("*", end = "")
    print("\n")