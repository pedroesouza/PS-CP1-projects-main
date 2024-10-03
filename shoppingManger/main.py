#Pedro Souza, Shopping Manager
list = []

def ask():
    action = input("What would you like to do now?\nEnter 1 to add item\nEnter 2 to remove item\nEnter 3 to leave the list:\n")
    if action == "1":
        add(input("What to you want to add?\n"))
    elif action == "2":
        remove(input("What to you want to remove?\n"))
        ask()
    elif action == "3":
        print("Have a nice day!")
        return True
    else:
        print("Invalid! Try again!")
        ask()

def add(thing):
    list.append(thing)
    print("Your list is:", list)
    ask()

def remove(thing):
    if thing in list:
        where = list.index(thing)
        list.pop(where)
        print("Your list is:", list)
        ask()
    else:
        print("Not in your list!")
        ask()

while True:
    if ask() == True:
        break