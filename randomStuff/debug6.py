
# The function should return True if the number is between 10 and 20 (inclusive), but it doesn't. Find the bug.

def is_between(num):

    if num >= 10 and num <= 20:

        return True

    return False

if is_between(int(input("What is your number?: "))):
    print("Your number is between 10-20")
else:
    print("Your number is not between 10-20")