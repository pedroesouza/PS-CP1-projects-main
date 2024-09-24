#Pedro Souza, anagram creator
import random
letters = list(input("Type your name: "))
for x in range(5):  random.shuffle(letters), print("".join(letters))