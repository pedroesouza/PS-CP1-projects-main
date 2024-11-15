import random
import operator


a = 0

n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

n3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

o1={
    '+': lambda p1, p3: p1 + p3, 
    '-': lambda p1, p3: p1 - p3,
    '*': lambda p1, p3: p1 * p3, 
    '/': lambda p1, p3: p1 / p3,}


p1 = random.choice(n1)
p2a, p2b = random.choice(list(o1.items()))
p3 = random.choice(n1)


q = f"{p1} {p2a} {p3}"


def ask(answer):
    try:
        float(a)
        return answer
    except:
        ask(input(f"Invalid, try again\n{q}"))

    

a = ask(input(f"{q}\n"))
a = float(a)

cA = float(p2b(p1, p3))


if a == cA:
    print("lmao ur right")
else:
    print(f"keep yourself safe, the correct answer was {cA}")