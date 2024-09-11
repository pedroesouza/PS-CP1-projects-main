import math
facultyAndStaff = 32
studentsAwarded = 100
guests = studentsAwarded * 2
tableSeats = 12
board = 0

studentsAwarded -= 1
facultyAndStaff -= 3
guests -= 15
board += 1

print("You will need", math.ceil((studentsAwarded + facultyAndStaff + guests + board) / tableSeats), "tables.")