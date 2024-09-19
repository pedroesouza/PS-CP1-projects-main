#Pedro Souza, Average grade
grade = 0
allGrades = 0
avgGrade = 0

classes = int(input("Amount of classes: "))

for amount in range(classes):
    print("Grade #", amount + 1, ":", sep = "", end = "")
    grade = int(input(""))
    allGrades += grade
    avgGrade = allGrades / (amount + 1)

print("Your average grade is ", avgGrade, "%", sep = "")