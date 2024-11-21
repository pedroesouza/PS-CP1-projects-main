#Pedro Souza, Error Handling Calculator

num1 = 0
num2 = 0

def ask1(a):
    try:
        int(a)
    except:
        a = ask1(input(input("INVALID, number 1: ")))

    else:
        int(a)

    return a


def ask2(a):
    try:
        int(a)
    except:
        a = ask2(input(input("INVALID, number 2: ")))

def ask3(a):
    try:
        int(a)

        if a not in [1, 2, 3, 4, 5]:
            num1 = ask3(input(input("INVALID, *(1), /(2), +(3). -(4), **(5): ")))
            break
        else:
            return a


    except:
        num1 = ask3(input(input("INVALID, *(1), /(2), +(3). -(4), **(5): ")))
        break


num1 = input("number 1: ")
num2 = ask2(input("number 2: "))
operator = ask3(input("*(1), /(2), +(3). -(4), **(5): "))


if operator == 1:
    print(f"Your answer is: {num1 * num2}")

if operator == 2:
    print(f"Your answer is: {num1 / num2}")

if operator == 3:
    print(f"Your answer is: {num1 + num2}")

if operator == 4:
    print(f"Your answer is: {num1 - num2}")

if operator == 5:
    print(f"Your answer is: {num1 ** num2}")
