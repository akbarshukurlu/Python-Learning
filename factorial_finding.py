print("""
**************************************

Welcome to the factorial calculation program.....

Press 'q' to exit.

**************************************
"""
)

# Start an infinite loop to keep asking user for input
while True:
    # Get input from the user
    number = input("Number:")

    # Check if the user wants to quit
    if (number == "q"):
        print("Exiting program....")
        break
    else:
        # Convert the input string to an integer
        number = int(number) 
        # Initialize the factorial result variable to 1
        factorial = 1

        # Multiply numbers from 1 up to the input number
        for i in range(1, number+1):
            factorial *= i

        # Print the final calculated factorial
        print("Faktoryal:", factorial)
