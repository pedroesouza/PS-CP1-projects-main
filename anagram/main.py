#Pedro Souza, anagram creator.
import random
name = input("Type your name: ")
letters = list(name)

for x in range(0, 6):
    random.shuffle(letters)
    newLetters = "".join(letters)
    print(newLetters)
