#Pedro Souza, Password validator


#\/ Variable setting.#
isLong = False
hasNum = False
hasSCharacter = False

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]
#/\#

#\/ Functions.#
def ask(password):

    password = list(password)

    pwLen = len(password)

    if pwLen >= 8:
        isLong = True
    else:
        isLong = False

    for i in password:
        if i not in numbers:
            hasNum = False
        else:
            hasNum = True
            break
        
    
    for x in password:
        if x not in sCharacters:
            hasSCharacter = False
        else:
            hasSCharacter = True
            break
        
    return isLong, hasNum, hasSCharacter
#/\#

#\/ Password ask and check loop.#
isLong, hasNum, hasSCharacter = ask(input("What is your password"))

while isLong == False or hasNum == False or hasSCharacter == False: 

    if isLong == False:
        print("Your passowrd is not long enough.")
    if hasNum == False:
        print("Your password needs to containt at least one number.")
    if hasSCharacter == False:
        print("Your password neeeds to contain a special character.")

    isLong, hasNum, hasSCharacter = ask(input("What is your new password"))

if isLong == True and hasNum == True and hasSCharacter == True:
    print("Your password is valid!")
#/\#
