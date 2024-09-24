#Pedro Souza, Pig latin translator

vowels = ["a", "e", "i", "o", "u"]
def translate(word):
    firstLetter = word[0]
    if firstLetter in vowels:
        word += "yay"
        print(word)
    else:
        wordList = list(word)
        wordList.append(firstLetter)
        wordList.pop(0)
        word = "".join(wordList)
        word += "yay"
        print(word)

translate(input("Your word: "))
