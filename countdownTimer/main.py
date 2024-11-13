import time

x = 1

def ask(answer):
    try:
        int(answer)

    except:
        y = ask(input("Invalid, try again:  "))

    return answer
    
y = ask(input("What is your number?:  "))

while x <= int(y):
    print(x)
    x += 1
    time.sleep(1)
