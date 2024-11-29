#Pedro Souza, Error Handling Calculator

def ask_o(operator):
    
    try:
        operator = int(operator)
    except:
        operator = ask_o(input("INVALID! (numbers only) What operation would you like to do: addition(1), subtraction(2), multiplication(3), or division(4)?"))

    return operator

def ask_n_1(num1):

    try:
        num1 = int(num1)
    except:
        num1 = ask_n_1(input("INVALID! (numbers only) Number 1: "))

    return num1

def ask_n_2(num2):

    if num2 == "0":
        if operator == 4:
            num2 = ask_n_2(input("INVALID! (you can't divide by 0) Number 2: "))

    try:
        num2 = int(num2)
    except:
        num2 = ask_n_2(input("INVALID! (numbers only) Number 2: "))

    return num2

operator = ask_o(input("What operation would you like to do: addition(1), subtraction(2), multiplication(3), or division(4)?"))

num1 = ask_n_1(input("Number 1: "))

num2 = ask_n_2(input("Number 2: "))

if operator == 1:
    print("The answer is:", num1+num2)

if operator == 2:
    print("The answer is:", num1-num2)

if operator == 3:
    print("The answer is:", num1*num2)

if operator == 4:
    print("The answer is:", num1/num2)
