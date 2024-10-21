import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) #Input was not inside int(), meaning it was a string. Syntax Bug. The program checks if guess is ">" a number later, and strings can't interact with said number (an integers) 
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            print("Game Over. Thanks for playing!") #Always said "game over". Logic Bug. The program would congratulate you on winning and then tell you "Game over", and term usually used to show someone lost the game (and yes, you just lost the game)
            game_over = True
            break #Even after you lost, the game would play one more time. Logic Bug. The game would give you more attemps than yo uwere supposed to
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1 #The attempts variable never went up. Logic Bug. If attempts never go up, you will never reach the maximum attempts, meaning you can't lose the game.
            print(f"Attempts: {str(attempts)}/{str(max_attempts)}")

        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts += 1
            print(f"Attempts: {str(attempts)}/{str(max_attempts)}")
        continue
start_game()