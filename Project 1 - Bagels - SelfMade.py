import random

def generateNumber():
    digit1 = random.randint(0,9)
    digit2 = random.randint(0,9)
    while digit2 == digit1:
        digit2 = random.randint(0,9)
    digit3 = random.randint(0,9)
    while int(digit3) == int(digit2) or int(digit3) == int(digit1):
        digit3=random.randint(0,9)
    
    secretNumber = str(digit1)+ str(digit2) + str(digit3)
    return secretNumber

def gameLogic():
    # i = 0
    # while i < 5:
    secretNumber = generateNumber()
    print('''Welcome to the game developed by Avirup.
    Game rules:
            You have to guess a 3 digit number.
            You will get a response as:
            Pico - If the any digit is correct but in wrong position.
            Fermi - If the any digit is correct and in correct position.
            Bagels - If the non of the digits are correct.

            You will have 10 guesses in total.
    ''')
    guesses = 10
    while True:
        user_guess = input("Enter your first guess > ")
        if len(user_guess) != 3:
            while True:
                user_guess = input("Invalid input. Enter 3 digit number. > ")
                if len(user_guess) == 3:
                    break
        guesses-=1
        if guesses == 0:
            print(f"You do not have any more guesses left. The number was {secretNumber}")
            playagain = input("Do you want to play again? (y/n)")
            if playagain == "y":
                print("-"*50)
                playgame()
            else:
                break
        if user_guess == secretNumber:
            print("Fermi! You guessed correctly.")
            playagain = input("Do you want to play again? (y/n)")
            if playagain == "y":
                print("-"*50)
                playgame()
            else:
                break
        i = 0
        for location, digit in enumerate(user_guess):
            if digit == secretNumber[i]:
                print("Fermi")
                i+=1
            elif digit != secretNumber[i] and digit in secretNumber:
                print("Pico")
                i+=1
            else:
                print("Bagels")
                i+=1
        print(f"You have {guesses} remaning.")


def playgame():
    generateNumber()
    gameLogic()

if __name__ == "__main__":
    playgame()