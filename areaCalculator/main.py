#Pedro Souza, Area calculator
def square_calc(side): return side^2
def rectangle_calc(width, height): return width * height
def triangle_calc(base, height): return (base * height)/2
def circle_calc(radius): return 3.14 * radius**2
def trapezoid_calc(base1, base2, height): return ((base1 + base2)/2)*height
shape = input("Square(1), Rectangle(2), Triangle(3), Circle(4), Trapezoid(5): ")
def ask():
    if shape == "1": print("The area of your square is", square_calc(float(input("Length of sides: "))))
    elif shape == "2": print("The area of your rectangle is", rectangle_calc(float(input("Width: ")), float(input("Height: "))))
    elif shape == "3": print("The area of your trangle is", triangle_calc(float(input("Base Lenght: ")), float(input("Height: "))))
    elif shape == "4": print("The area of your circle is aproximatelly", circle_calc(float(input("Radius: "))))
    elif shape == "5": print("The area of your trapezoid is", trapezoid_calc(float(input("First base lenght: ")), float(input("Second base lenght")), float(input("Height: "))))
    else: print("Invalid"), ask()
ask()