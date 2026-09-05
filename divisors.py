print("""
****************
Finding the divisors of a number.

Press 'q' to exit.
****************
""")

def get_divisors(number):
    get_divisors = []


    for i in range(1, number):

        if (number % i == 0):
            get_divisors.append(i)

    return get_divisors

while True:
    number = input("Your Count:")

    if (number == "q"):
        print("Exiting program....")
        break
    else:
        number = int(number)
        print("Divisors: ", get_divisors(number))