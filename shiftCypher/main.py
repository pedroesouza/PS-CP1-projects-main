#Pedro Souza, Shift cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(word):
    wordList = list(word)
    alphabet.find(wordList)
    wordList.pop(0)
    word = "".join(wordList)
    print(word)

encode(input("What is your word: "))