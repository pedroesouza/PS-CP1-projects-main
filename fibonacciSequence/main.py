#Pedro Souza, Fibonacci Sequence

#define new variables
num1 = 0
num2 = 0
num3 = 0
numString = ""
numCount = 0

#questions
starter = int(input("What is the starting number after 0? "))
amount = int(input("How many numbers will it show? "))

#start the first 2 numbers
num2 = starter
numString = str(num1) + ", " + str(num2)

#amount of times its going -2 (they were done at the start the first 2 numbers part)
finalAmount = amount - 2

#calculation
for x in range(finalAmount):
    #add num2 and num1 to make num 3, add num3 to string, make num1 num2, make num2 num3
    num3 = num1 + num2
    numString += ", " + str(num3)
    num1 = num2
    num2 = num3

#print when loop is done
print(numString)