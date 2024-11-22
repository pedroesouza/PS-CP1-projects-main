#Pedro Souza, quiz game

import random
import operator


a = 0
cA = 0
c = True
r = "m"

oP_s = {}

n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

n3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

n4 = [x * 0.5 for x in range(4, 1001)]

n5 = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5,
    10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5,
    17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0,
    23.5, 24.0, 24.5, 25.0]

o1={
    '+': lambda p1, p3: p1 + p3, 
    '-': lambda p1, p3: p1 - p3}

o2={
    '+': lambda p1, p3: p1 + p3, 
    '-': lambda p1, p3: p1 - p3,
    '*': lambda p1, p3: p1 * p3, 
    '/': lambda p1, p3: p1 / p3,}

o3={
    '+': lambda p1, p3: p1 + p3, 
    '-': lambda p1, p3: p1 - p3,
    '*': lambda p1, p3: p1 * p3, 
    '/': lambda p1, p3: p1 / p3,
    '**': lambda p1, p3: p1 ** p3}

def easy():
    p1 = random.choice(n1)
    p2a, p2b = random.choice(list(o1.items()))
    p3 = random.choice(n1)

    q = f"{p1} {p2a} {p3}"

    cA = float(p2b(p1, p3))

    op_s = {cA, cA - random.choice(n4), cA + random.choice(n4), cA / random.choice(n5), cA * random.choice(n5)}

    a = ask(input(f"{q}\noptions: {op_s}\n"))
    a = float(a)

    if a == cA:
        print("Correct")
        return True
    else:
        print(f"Wrong, the correct answer was {cA}")
        return False


def medium():
    p1 = random.choice(n2)
    p2a, p2b = random.choice(list(o2.items()))
    p3 = random.choice(n2)

    q = f"{p1} {p2a} {p3}"

    cA = float(p2b(p1, p3))

    op_s = {cA, cA - random.choice(n4), cA + random.choice(n4), cA / random.choice(n5), cA * random.choice(n5)}

    a = ask(input(f"{q}\noptions: {op_s}\n"))
    a = float(a)

    if a == cA:
        print("Correct")
        return True
    else:
        print(f"Wrong, the correct answer was {cA}")
        return False



def hard():
    p1 = random.choice(n3)
    p2a, p2b = random.choice(list(o3.items()))
    p3 = random.choice(n3)

    q = f"{p1} {p2a} {p3}"

    cA = float(p2b(p1, p3))

    op_s = {cA, cA - random.choice(n4), cA + random.choice(n4), cA / random.choice(n5), cA * random.choice(n5)}

    a = ask(input(f"{q}\noptions: {op_s}\n"))
    a = float(a)

    if a == cA:
        print("Correct")
        return True
    else:
        print(f"Wrong, the correct answer was {cA}")
        return False

def ask(answer):
    try:
        float(a)
        return answer
    except:
        ask(input(f"Invalid, try again\n{q}"))

c = medium()
q2 = input("Want to end? (Y or N): ").lower()
if q2 == "y":
    print("\nGoodbye!\n")
    exit()
else:
    pass

while True:
    if r == "m":
        if c == True:
            c = hard()
            r = "h"
        else:
            c == easy()
            r = "c"

        q2 = input("Want to end? (Y or N): ").lower()
        if q2 == "y":
            print("\nGoodbye!\n")
            exit()
        else:
            pass

    if r == "e":
        if c == True:
            c = medium()
            r = "m"
        if c == False:
            c = easy()
            r = "e"

        q2 = input("Want to end? (Y or N): ").lower()
        if q2 == "y":
            print("\nGoodbye!\n")
            exit()
        else:
            pass

    if r == "h":
        if c == True:
            c = hard()
            r = "h"
        if c == False:
            c = easy()
            r = "e"
    
        q2 = input("Want to end? (Y or N): ").lower()
        if q2 == "y":
            print("\nGoodbye!\n")
            exit()
        else:
            pass