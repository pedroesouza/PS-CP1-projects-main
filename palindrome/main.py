#Pedro Souza, Palindrome

def check(word):
    if word == word[::-1]:
        return True

if check(input("What word do you want to check?\n")) == True:
    print("Yup, its a palendrome")
else:
    print("Not a palendrome")