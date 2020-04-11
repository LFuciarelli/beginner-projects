def operation():
    """
    :return: Returns a number between 1 and 5 that represents the four fundamental mathematical operations and exit.
    """
    print("Choose an option:")
    print("[1] Addition (+)")
    print("[2] Subtraction (-)")
    print("[3] Multiplication (*)")
    print("[4] Division (/)")
    print("[5] Exit")
    while True:
        try:
            option = int(input("Enter the number of the operation: "))
            while not 1 <= option <= 5:
                option = int(input("[ERROR] Enter a number present among the options: "))
            return option
        except (TypeError, ValueError):
            print("[ERROR] Your option has to be an integer")


print("Text-based calculator")

while True:                                                                        # Loop for the first number
    try:
        tot = float(input("Enter a number: "))
        break
    except (TypeError, ValueError):
        print("[ERROR] The value has to be an integer or a decimal number.")

while True:                                                                         # Main loop
    operator = operation()
    if operator < 5:                                                                # Verifies whether the user wants
        while True:                                                                 # to exit or not
            try:
                number = float(input("Enter a number: "))
                break
            except (TypeError, ValueError):
                print("[ERROR] The value has to be an integer or a decimal number")
        if operator == 1:                                                           # Addition
            tot += number
        elif operator == 2:                                                         # Subtraction
            tot -= number
        elif operator == 3:                                                         # Multiplication
            tot *= number
        else:                                                                       # Division
            tot /= number
    if tot == int(tot):                                                             # It is just to avoid writing
        print(int(tot))                                                             # integers as floats (e.g. 6.0
    else:                                                                           # instead of 6)
        print(tot)
