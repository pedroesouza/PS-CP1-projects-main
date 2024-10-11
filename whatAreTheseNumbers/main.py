#Pedro Souza, What are these numbers
num1 = int(input("What is the number that you want to add commas to separeate the thousands?: "))
num2 = int(input("What is the number that you want to turn into a float with 4 decimal places?: "))
num3 = float(input("What is the number that you want to turn into a percentage?: "))
num4 = float(input("What is the number that you want to turn into a dollar ammount?: "))

print(("{:,}".format(num1)))
print(("{:.4f}".format(num2)))
print(("{:.1%}".format(num3)))
print("$" + str(("{:,.2f}".format(num4))))