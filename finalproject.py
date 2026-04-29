import random



def get_difficulty(): #makes sure the user enters a correct difficulty level

    level = input("Enter 'Easy', 'Medium', or 'Hard' mode: ").lower()

    while level not in ['easy', 'medium', 'hard']:
        print("invalid difficulty mode, try again")
        level = input("Enter 'Easy', 'Medium', or 'Hard' mode: ").lower()

    return level


def get_guess():

    userinput = (input("enter a number between 1 and 100: "))

    while not userinput.isdigit() or not (1<= int(userinput) <=100): #makes sure userinput is a digit and within 1 and 100
        print("invalid input, try again")
        userinput = (input("enter a number between 1 and 100: "))

    return int(userinput)


def game():

    number = random.randint(1,100) #generating the number
    guesses = [] #this list will store all the guesses the user makes

    level = get_difficulty()

    #setting the difficulty level by restricting maximum number of attempts allowed
    if level == "easy":
        max_attempts = 10
    elif level == "medium":
        max_attempts = 7
    else:
        max_attempts = 5

    print(f"you have {max_attempts} attempts to guess the number")

    attempts = 0

    while attempts < max_attempts: #keep checking if guess is correct until there are no more attempts left

        userinput = get_guess()
        attempts += 1
        guesses.append(userinput)

        if userinput == number:

            print("You Win!")
            print(f"the number was {number}, it took you {len(guesses)} attempts ")
            print(f"your guesses were: {guesses}")
            return None #to stop when the user guesses correctly

        elif userinput > number:
            print("Too high")
        else:
            print("Too low")

    print("No more attempts left")
    print(f"the number was {number}")
    print(f"your guesses were: {guesses}")


def main():
    game()

    replay = input("do you want to play again, enter yes or no: ").lower()

    while replay not in ["yes", "no"]: #validating replay
        print("invalid input, try again")
        replay = input("do you want to play again, enter yes or no: ").lower()

    while replay == "yes":
        game()
        replay = input("do you want to play again, enter yes or no: ").lower()
        while replay not in ["yes", "no"]:
            print("invalid input, try again")
            replay = input("do you want to play again, enter yes or no: ").lower()
        


if __name__ == "__main__":
    main()


        



