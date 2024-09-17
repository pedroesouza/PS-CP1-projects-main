#Pedro Souza, Graded Quiz
score = 0
question1 = int(input("Infinite bacon but no games(1), or games, infinite games, but no games(2)? "))
question2 = int(input("Where is paris? France(1) not France(2): "))
question3 = int(input("Where is waldo? France(1), on the book(2): "))
question4 = int(input("Im blue. Badabi badaba(1), I'm a smurf(2): "))
question5 = int(input("Only in North Dakota(1), Ohio(2): "))

if question1 == 1:
    score += 1
if question2 == 1:
    score += 1
if question3 == 2:
    score += 1
if question4 == 1:
    score += 1
if question5 == 2:
    score += 1

print("score:", score)