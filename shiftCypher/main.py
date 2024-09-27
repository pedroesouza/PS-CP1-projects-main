#Pedro Souza, Shift cypher

alphabet = "  abcdefghijklmnopqrstuvwxyzaABCDEFGHIJKLMNOPQRSTUVWXYZA0123456789012"

def encode(word):
    wordLen = len(word)
    newWord = []
    repeats = 0
    for x in word:
        letter = x
        whereLetter = alphabet.index(letter)
        newWord.insert(repeats, alphabet[whereLetter + 1])
        word = "".join(newWord)
        repeats += 1
    print("encoded:",word)

encode(input("What is your word to encode: "))