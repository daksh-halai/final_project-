import random

number = random.randint(1,100)

userinput = int(input("enter a number between 1 and 100: "))

while type(userinput) != int and 1<= userinput <=100:
    print("invalid input, try again")
    userinput = int(input("enter a number between 1 and 100: "))




