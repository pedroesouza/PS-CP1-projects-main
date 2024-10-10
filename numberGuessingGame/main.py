#Number guessing game, Pedro Souza

import random #Imports random
num = random.randint(1, 10) #Generates random number
guess = int(input("What is your guess (Numbers 1-10)?: ")) #Creates guess variable

while guess != num: #Repeat if they didnt guess right
    print("You are incorrect, try again!") #Tell them they are incorrect
    guess = int(input("What is your guess?: ")) #Ask them for new guess

print("Correct!") #Tell them they are correct when the incorrect guess program stops repeating