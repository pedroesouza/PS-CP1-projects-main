#Pedro Souza, Pig latin translator

vowels = ["a", "e", "i", "o", "u"]
def translate(word):
    firstLetter = word[0]
    if firstLetter in vowels:
        print("Original word:", word)
        word += "yay"
        print(word)
    else:
        wordList = list(word)
        while firstLetter not in vowels:
            wordList.append(firstLetter)
            wordList.pop(0)
            firstLetter = wordList[0]

        print("Original word:", word)
        word = "".join(wordList)
        word += "ay"
        print("Pig latin translation:", word)

translate(input("Your word (please all lowercase): "))