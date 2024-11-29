#Pedro Souza, Count up and down

#\/ Importing#
import time
#/\#

#\/ Variable setting.#
condition = True

num = -1
#/\#


while True:

    #\/ Condition is a boolean which is True, but turns false when the counting number reaches 20.#
    if num == 20:
        condition = False
    #/\#

    #\/ Two if statements, one counts up, and one down, which statement runs depends on the *condition* value.#
    if condition == True:
        num += 1
        print(num)
        time.sleep(1)

    if condition == False:
        num -= 1
        print(num)
        time.sleep(1)

        #\/ Ends the code when done counting.#
        if num == 0:
            exit()
        #/\#
    #/\#
