#Pedro Souza, Personal Information Converter
name = input("Hello! What is your name? ")
print("Nice to meet you ", name, "!", sep = "")
age = input("How old are you? ")
height = input("Cool! How tall are you (in meters please)? ")
favNum = input("And last question, what is your favourite number? ")

print("OG values = ", name, ", ", age, ", ", height, ", ", favNum, ".", sep = "")
print("Converted values = ", str(name), ", ", int(age), ", ", float(height), ", ", int(favNum), ".", sep = "")