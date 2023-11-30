# Task 1.1 - ISBN-6

def six_digit_isbn():
    # Take a 6-digit input from the user
    user_input = input("Enter a 6-digit number: \n")

    # Split the input into an array (list) of digits
    d = [int(digit) for digit in user_input]

    # Checks it is a valid code
    if len(d) < 5 or len(d) > 6:

        print("Enter valid 6 digit code.")
        six_digit_isbn() # Uses recursion to start again if invalid input

    # Adds error correction digit if needed
    if len(d) == 5:
        remainder = (d[0]+d[1]+d[2]+d[3]+d[4]) % 5
        bongo = 5 - remainder
        print("\nAdding", bongo, "to array.")
        d.append(bongo)

    # Checks if valid ISBN num
    if len(d) == 6:
        if (6 * d[0] + 5 * d[1] + 4 * d[2] + 3 * d[3] + 2 * d[4] + 1 * d[5]) % 7 == 0:
            print("\nValid ISBN.\n")
        else:
            print("\nInvalid  ISBN.\n")


six_digit_isbn()
