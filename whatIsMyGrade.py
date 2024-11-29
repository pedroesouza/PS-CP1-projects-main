#Pedro Souza, what is my grade

gList = []
nList = []


def ask_grade(name, grade):

    nList.append(name)
    gList.append(grade)


numClasses = int(input("\nHow many classes do you have?:\n"))


for currClass in range(1, numClasses + 1):

    ask_grade(input(f"\nWhat is the name of class #{currClass}?:\n"), float(input(f"\nWhat your grade in #{currClass}?:\n")))

print("\n")

for printClass in range(numClasses):

    if gList[printClass] >= 94:
        letterGrade = "A"

    elif gList[printClass] >= 90:
        letterGrade = "A-"

    elif gList[printClass] >= 87:
        letterGrade = "B+"

    elif gList[printClass] >= 84:
        letterGrade = "B"

    elif gList[printClass] >= 80:
        letterGrade = "B-"

    elif gList[printClass] >= 77:
        letterGrade = "C+"

    elif gList[printClass] >= 74:
        letterGrade = "C"

    elif gList[printClass] >= 70:
        letterGrade = "C-"

    elif gList[printClass] >= 67:
        letterGrade = "D+"

    elif gList[printClass] >= 64:
        letterGrade = "D"
        
    elif gList[printClass] >= 60:
        letterGrade = "D-"

    else:
        letterGrade = "F"

    print(f"{nList[printClass]}: {letterGrade}")

print("\n")
