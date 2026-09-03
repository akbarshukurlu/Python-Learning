print("""
**************************
Welcome to the Fibonacci Calculation Program....

Press 'q' to exit.

**************************
""")

while True:
    number = input("Your Number:")

    if (number == "q"):
        print("Exiting Program....")
        break
    else:
        number = int(number) 
        a = 1
        b = 1
        fibonacci = [ a , b]

        for i in range(number -2):
            a,b = b,a+b
            fibonacci.append(b)


        print("Fibonacci: ", fibonacci)
            
        
    
        