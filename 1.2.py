# Task 1.2 - BCH Generating and Correcting.


# Generates parity data for valid BCH code
def generator():

    # Input 6 digits
    user_input = input("Enter a 6-digit number: \n")

    # Define list d
    d = []

    # Check if the input is exactly 6 digits
    if len(user_input) != 6 or not user_input.isdigit():
        print("Please enter a valid 6-digit number.")
    else:
        # Split the input into an array (list) of digits
        d = [int(digit) for digit in user_input]

    # Appends the redundancy digits, based on relevant formulas.
    d.append((4 * d[0] + 10 * d[1] + 9 * d[2] + 2 * d[3] + 1 * d[4] + 7 * d[5]) % 11)
    d.append((7 * d[0] + 8 * d[1] + 7 * d[2] + 1 * d[3] + 9 * d[4] + 6 * d[5]) % 11)
    d.append((9 * d[0] + 1 * d[1] + 7 * d[2] + 8 * d[3] + 7 * d[4] + 7 * d[5]) % 11)
    d.append((1 * d[0] + 2 * d[1] + 9 * d[2] + 10 * d[3] + 4 * d[4] + 1 * d[5]) % 11)

    usable = True

    # Checks if any digits that have been appended are greater than 10
    for i in d[6:]:
        if i >= 10:
            print("\nUnusable number")
            usable = False
            break

    # If all numbers are valid then call decoder()
    if usable:
        print(d)


# Decodes BCH code
def decoder(codeword):

    # List of numbers with no square root
    no_s = [2, 6, 7, 8, 10]

    twoOrLessErrors = True
    while twoOrLessErrors:

        # Creates syndromes 1-4 using formulas respectively
        syndrome_1 = ((1*codeword[0]) + (1*codeword[1]) + (1*codeword[2]) + (1*codeword[3]) + (1*codeword[4]) + (1*codeword[5]) + (1*codeword[6]) + (1*codeword[7]) + (1*codeword[8]) + codeword[9]) % 11
        syndrome_2 = ((1*codeword[0]) + (2*codeword[1]) + (3*codeword[2]) + (4*codeword[3]) + (5*codeword[4]) + (6*codeword[5]) + (7*codeword[6]) + (8*codeword[7]) + (9*codeword[8]) + (10*codeword[9])) % 11
        syndrome_3 = ((1*codeword[0]) + (4*codeword[1]) + (9*codeword[2]) + (5*codeword[3]) + (3*codeword[4]) + (3*codeword[5]) + (5*codeword[6]) + (9*codeword[7]) + (4*codeword[8]) + (1*codeword[9])) % 11
        syndrome_4 = ((1*codeword[0]) + (8*codeword[1]) + (5*codeword[2]) + (9*codeword[3]) + (4*codeword[4]) + (7*codeword[5]) + (2*codeword[6]) + (6*codeword[7]) + (3*codeword[8]) + (10*codeword[9])) % 11

        # Creates P,Q,R for single and double error correction
        p = ((syndrome_2 ** 2) - (syndrome_1 * syndrome_3)) % 11
        q = ((syndrome_1 * syndrome_4) - (syndrome_2 * syndrome_3)) % 11
        r = ((syndrome_3 ** 2) - (syndrome_2 * syndrome_4)) % 11
        print("p, q, r:\n", p, q, r)
        print("syndromes 1-4:\n", syndrome_1, syndrome_2, syndrome_3, syndrome_4)

        if syndrome_1 == 0 and syndrome_2 == 0 and syndrome_3 == 0 and syndrome_4 == 0:  # Checks no error occurred

            print("\n", codeword)
            print("no error\n")
            twoOrLessErrors = False  # Stops the While Loop

        elif p == 0 and q == 0 and r == 0:  # Checks if single error occurred

            magnitude = syndrome_1
            inverse = 0  # value of s1 multiplied
            holder = 0  # will be what s1 is multiplied by

            while inverse != 1:
                holder += 1
                y = syndrome_1 * holder
                inverse = y % 11

            # Calculates the error position
            err_pos = (syndrome_2 * holder) % 11

            # Fixes error at correct position by the calculated magnitude
            codeword[err_pos - 1] -= magnitude

            # Printing out values
            print("\nHolder: ", inverse)
            print("Mag:", magnitude)
            print("\nerror position", err_pos)

            # Prints out new fixed codeword
            print("\nSingle error,\nNew codeword:\n", codeword)
            twoOrLessErrors = False  # Stops the While Loop

        elif p != 0 or q != 0 or r != 0:  # if there are 2 errors

            # Finding i value
            i1 = ((q**2)-(4*p*r)) % 11
            if i1 % 11 in no_s or (i1 % 11) > 10:
                print("\nTwo or more errors\n")
                break
            else:
                sq1 = 1
                while (sq1 * sq1) % 11 != i1:
                    sq1 += 1

            i2 = (2*p) % 11
            i3 = (-q + sq1) % 11
            y = 1

            while (i2 * y) % 11 != 1:
                y += 1

            i = (i3 * y) % 11

            # Finding j Value
            j1 = ((q**2)-(4*p*r)) % 11
            if j1 % 11 in no_s or (j1 % 11) > 10:
                print("\nTwo or more errors\n")
                break
            else:
                sq2 = 1
                while (sq2 * sq2) % 11 != j1:
                    sq2 += 1

            j2 = (2*p) % 11
            j3 = (-q - sq2) % 11
            y = 1

            while (i2 * y) % 11 != 1:
                y += 1

            j = (j3 * y) % 11

            bp2 = (i - j) % 11
            y = 1

            while ((bp2) * y) % 11 != 1:
                y += 1

            bp1 = (i * syndrome_1) % 11
            hh = (bp1 - syndrome_2) % 11

            # Work out the 2 error magnitudes
            b = int((hh * y) % 11)
            a = int(syndrome_1 - b) % 11

            old_i = codeword[i - 1]
            new_i = (old_i - a) % 11

            old_j = codeword[j - 1]
            new_j = (old_j - b) % 11

            codeword[i - 1] = new_i
            codeword[j - 1] = new_j

            print("\nPosition 1 (i): ", i, " Magnitude a: ", a)
            print("\nPosition 2 (j): ", j, " Magnitude b: ", b)
            print("\nDouble error,\nNew codeword:\n", codeword)
            twoOrLessErrors = False # Stops the While Loop


generator()
