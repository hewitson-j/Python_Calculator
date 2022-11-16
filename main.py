import re

num1 = input("First number: ")
op = input("""Type in the corresponding number to the operation: 
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Exponent
""")
num2 = input("Second number: ")

try:
    num1 = re.sub('\D', '', num1)
    num2 = re.sub('\D', '', num2)
    op = re.sub('\D', '', op)

    num1 = int(num1)
    num2 = int(num2)
    op = int(op)
except:
    print("Input not valid. Please try again.")
    exit()

match op:
    case 1:
        confirmation = input("Requested operation: " + str(num1) + " + " + str(num2) + """

Is this correct? Type 'y' or 'n'.
""")
        confirmation = confirmation.upper()

        if confirmation == 'Y':
            print("Answer: ", str(num1 + num2), """
            
Thank you. Start program again to calculate another value.""")
        elif confirmation == "N":
            print ("Operation cancelled. Closing program.")
            exit()

    case 2:
        confirmation = input("Requested operation: " + str(num1) + " - " + str(num2) + """

Is this correct? Type 'y' or 'n'.
    """)
        confirmation = confirmation.upper()

        if confirmation == 'Y':
            print("Answer: ", str(num1 - num2), """
            
Thank you. Start program again to calculate another value.""")
        elif confirmation == "N":
            print("Operation cancelled. Closing program.")
            exit()

    case 3:
        confirmation = input("Requested operation: " + str(num1) + " * " + str(num2) + """

Is this correct? Type 'y' or 'n'.
    """)
        confirmation = confirmation.upper()

        if confirmation == 'Y':
            print("Answer: ", str(num1 * num2), """
            
Thank you. Start program again to calculate another value.""")
        elif confirmation == "N":
            print("Operation cancelled. Closing program.")
            exit()

    case 4:
        confirmation = input("Requested operation: " + str(num1) + " / " + str(num2) + """

Is this correct? Type 'y' or 'n'.
    """)
        confirmation = confirmation.upper()

        if confirmation == 'Y':
            print("Answer: ", str(num1 / num2), """
            
Thank you. Start program again to calculate another value.""")
        elif confirmation == "N":
            print("Operation cancelled. Closing program.")
            exit()

    case 5:
        confirmation = input("Requested operation: " + str(num1) + " ^ " + str(num2) + """

Is this correct? Type 'y' or 'n'.
    """)
        confirmation = confirmation.upper()

        if confirmation == 'Y':

            print("Answer: ", str(pow(num1, num2)), """
            
Thank you. Start program again to calculate another value.""")
        elif confirmation == "N":
            print("Operation cancelled. Closing program.")
            exit()