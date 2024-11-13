import random
import operator

n1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"]

o1={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}

p1 = random.choice(n1)
p2 = random.choice()
p3 = random.choice(n1)
q = f"{p1} {p2.key} {p3}"

a = input(q)
cA = p2.value(p1, p2)
