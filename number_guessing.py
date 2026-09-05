import random
import time

print("""
**************************************
Number guessing game

Guess a number between 1 and 40

**************************************
""")

random_number = random.randint(1,40)
guesses_left = 7
while True:
    taxmin = int(input("Your guess:"))

    if (taxmin < random_number):
        print("Checking information......")
        time.sleep(1)
        print("Enter a higher number.....")
        guesses_left -= 1
    elif (taxmin > random_number):
        print("Checking information......")
        time.sleep(1)
        print("Enter a lower number....")
        guesses_left -= 1

    else: 
        print("Checking information.....")
        time.sleep(1)
        print("Congratulations! The number:", random_number)
        break
    if (guesses_left == 0):
        print("Out of guesses...")
        print("The number:", random_number)
        break



