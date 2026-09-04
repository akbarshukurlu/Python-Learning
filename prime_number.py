print("""
****************
Finding  Whether a number is prime or not

Press 'q' to exit.
****************
""")

def primenumber(number):
    if (number == 1):
        return False
    elif (number == 2):
        return True

    else:
        for i in range(2,number):
            if (number % i == 0):
                return False
        return True

while True:
    number = input("Your Count:")

    if (number == "q"):
        break
    else:
        number = int(number)

        if (primenumber(number)):
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")
            