import time

x = 0

def ask(answer):
    try:
        int(answer)

    except:
        y = ask(input("Invalid, try again:  "))

    return answer
    
y = ask(input("What is your number?:  "))
y = int(y)

while y >= x:
    print(y)
    y -= 1
    time.sleep(1)
