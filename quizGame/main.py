#Pedro Souza, Simple Quiz Game

#q1 = input("How long was the Seven Years' War?\n\n    A) 7 years\n    B) 8 years\n    C) 9 years\n    D) 100 years\n\n Your answer: ")

#q2 = input("How long was was the Ten Years' war?\n\n    A) 9 years\n    B) 10 years\n    C) 15 years\n    D) 21 years\n\n Your answer: ")

#q3 = input("How long was was the Eighty Years' war?\n\n    A) 80 years\n    B) 20 years\n    C) 15 years\n    D) 21 years\n\n Your answer: ")

#q4 = input("How long was was the Three Hundred and Thirty Five Years' War?\n\n    A) 335 Months\n    B) 335 years\n    C) 0.5 years\n    D) 80 years\n\n Your answer: ")

#q5 = input("How long was was the Hundred Years' War?\n\n    A) 100 years\n    B) 10 years\n    C) 116 years\n    D) 80 years\n\n Your answer: ")

#q6 = input("6 * 8 - 10(15)?\n\n    A) 104\n    B) 80\n    C) -98\n    D) -105\n\n Your answer: ")

def ask():
    q4 = input("How long was was the Three Hundred and Thirty Five Years' War?\n\n    A) 335 Months\n    B) 335 years\n    C) 0.5 years\n    D) 80 years\n\n Your answer: ")
    if q4 == questions["q4"]:
        print("cool")


questions = {
    "q1": {"d": "easy", "a": "A"},
    "q2": {"d": "easy", "a": "B"},
    "q3": {"d": "easy", "a": "A"},
    "q4": {"d": "mid", "a": "B"},
    "q5": {"d": "hard", "a": "C"},
    "q6": {"d": "mid", "a": "D"}
    }

ask()