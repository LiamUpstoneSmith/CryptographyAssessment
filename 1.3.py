# Task 1.3  - Brute Force Password Cracking

import itertools
import hashlib
import time


# User input hashed password to crack
hashed_password = input("\nEnter hashed password:\n")


# SHA1 hashes given input
def sha1_hash(thing):
    hasher = hashlib.sha1(thing.encode())
    c = hasher.hexdigest()
    return c


def set_a(check):

    # Starts timer
    start_time = time.time()

    num_letters = 0

    # Check if password is 1 character long
    for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=1):
        c = ''.join(combination)
        print(c)
        c = sha1_hash(c)
        if c == check:
            answer = ''.join(combination)
            print("-------------------------------\n" + answer + "\n-------------------------------")
            num_letters = 0
            end_time = time.time()
            break
        else:
            for i in range(1000):  # Hashes combination up to 1000th level
                c = sha1_hash(c)
                if c == check:
                    answer = ''.join(combination)
                    print("-------------------------------\n", answer, "Hashed in :", i,
                          "\n-------------------------------")
                    num_letters = 0
                    end_time = time.time()
                    break
                else:
                    num_letters = 1

    # Check if password is 2 characters long
    if num_letters == 1:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=2):
            c = ''.join(combination)
            print(c)
            c = sha1_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination up to 1000th level
                    c = sha1_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        num_letters = 0
                        end_time = time.time()
                        break
                    else:
                        num_letters = 2

    # Check if password is 3 characters long
    if num_letters == 2:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=3):
            c = ''.join(combination)
            print(c)
            c = sha1_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination up to 1000th level
                    c = sha1_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        num_letters = 0
                        end_time = time.time()
                        break
                    else:
                        num_letters = 3

    # Check if password is 4 characters long
    if num_letters == 3:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=4):
            c = ''.join(combination)
            print(c)
            c = sha1_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination up to 1000th level
                    c = sha1_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        num_letters = 0
                        end_time = time.time()
                        break
                    else:
                        num_letters = 4

    # Check if password is 5 characters long
    if num_letters == 4:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=5):
            c = ''.join(combination)
            print(c)
            c = sha1_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination up to 1000th level
                    c = sha1_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        num_letters = 0
                        end_time = time.time()
                        break
                    else:
                        num_letters = 5

    # Check if password is 6 characters long
    if num_letters == 5:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=6):
            c = ''.join(combination)
            print(c)
            c = sha1_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination up to 1000th level
                    c = sha1_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        num_letters = 0
                        end_time = time.time()
                        break
                    else:
                        num_letters = 0

    # Calculates and prints time taken for algorithm to complete
    overall_secs = end_time - start_time
    overall_mins = overall_secs / 60
    overall_secs = round(overall_secs, 2)
    overall_mins = round(overall_mins, 2)
    print("\n", overall_secs, " Seconds to complete")
    print("\n", overall_mins, " mins to complete")


# Checks if code is valid isbn number
def valid_isbn(check):

    # Split the input into an array (list) of digits
    d = [int(digit) for digit in check]

    # Checks it is a valid code
    if len(d) < 5 or len(d) > 6:
        print("Enter valid 6 digit code.")
        valid_isbn(check)

    # Checks if valid ISBN num
    else:
        if (1 * d[0] + 2 * d[1] + 3 * d[2] + 4 * d[3] + 5 * d[4] + 6 * d[5]) % 7 == 0:
            return True
        else:
            return False


def set_b(check):

    # Starts timer
    start_time = time.time()

    # Checks every combination of length 6
    for combination in itertools.product('0123456789', repeat=6):
        c = ''.join(combination)
        print(c)

        # checks if combination is valid ISBN-6 number
        if valid_isbn(c):
            c = sha1_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination up to 1000th level
                    c = sha1_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        end_time = time.time()
                        break

    # Calculates and prints time taken for algorithm to complete
    overall_secs = end_time - start_time
    overall_mins = overall_secs / 60
    overall_secs = round(overall_secs, 2)
    overall_mins = round(overall_mins, 2)
    print("\n", overall_secs, " Seconds to complete")
    print("\n", overall_mins, " mins to complete")


# Creates Valid BCH parity bits based on input
def valid_bch(combo):

    # Define list d
    d = []

    d = [int(digit) for digit in combo]

    # Appends the redundancy digits, based on relevant formulas.
    d.append((4 * d[0] + 10 * d[1] + 9 * d[2] + 2 * d[3] + 1 * d[4] + 7 * d[5]) % 11)
    d.append((7 * d[0] + 8 * d[1] + 7 * d[2] + 1 * d[3] + 9 * d[4] + 6 * d[5]) % 11)
    d.append((9 * d[0] + 1 * d[1] + 7 * d[2] + 8 * d[3] + 7 * d[4] + 7 * d[5]) % 11)
    d.append((1 * d[0] + 2 * d[1] + 9 * d[2] + 10 * d[3] + 4 * d[4] + 1 * d[5]) % 11)

    return d


def set_c(check):

    # Starts timer
    start_time = time.time()

    # Checks every combination of length 6
    for combination in itertools.product('0123456789', repeat=6):
        c = ''.join(combination)
        print(c)

        # Creates BCH code from input
        d = valid_bch(combination)

        # Checks if numbers are usable (no number is greater than 10)
        for i in d[6:]:
            if i >= 10:
                usable = False
                break
            else:
                usable = True

        if usable:
            c = ''.join(map(str, d))
            c = sha1_hash(c)
            if c == check:
                answer = ''.join(str(d))
                print("-------------------------------\n" + answer + "\n-------------------------------")
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination up to 1000th level
                    c = sha1_hash(c)
                    if c == check:
                        answer = ''.join(d)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        end_time = time.time()
                        break

    # Calculates and prints time taken for algorithm to complete
    overall_secs = end_time - start_time
    overall_mins = overall_secs / 60
    overall_secs = round(overall_secs, 2)
    overall_mins = round(overall_mins, 2)
    print("\n", overall_secs, " Seconds to complete")
    print("\n", overall_mins, " mins to complete")


set_c(hashed_password)

"""

Set A Test Cases:   2,341,295 possible combinations

MAKE  --  1029 seconds  --  17.16 mins  --  5f4395a75c71fe04b6156d6290da65a27f17e138

1YOUR1  --  49523 seconds  --  825.4 mins  --  13.75 hours  --  16607928013478be20d30ccd60d958149bd48541

PWD5  --  1268 seconds  --  21.14 mins  --  74fcb3939fb7460f1e6a00a32ca45510ebff9ffa

LONGER  --  75734 seconds  --  1262 mins --  21.03 hours  --  88765f800a890eef93767f976eca17f91cbf85ea

4 --  6.51 seconds --  1b6453892473a467d07372d45eb05abc2031647a

BETTER  --  70725 seconds  --  1178.76 mins  --  19.65 hours  --  3bb9cdac38c5c43cd6cbe4752c40041d58894545

SECRET  --  75187 seconds  --  1253.13 mins  --  20.89 hours  --  3c3b274d119ff5a5ec6c1e215c1cb794d9973ac1

"""

"""

Set B Test Cases:

123456  --  16.14 seconds  -- 7c4a8d09ca3762af61e59520943dc26494f8941b

987654  --  130.87 seconds  --  dea742e166979027ae70b28e0a9006fb1010e760

381241  --  49.86 seconds  --  68952957dede23fe1fe06eb71d97f01bacb34197

999992  --  132.01 seconds  -- 2a81b68e789b1a4681e05d1d3dc1a73625b8e5eb

246804  --  32.26 seconds  --  1b88ec85ffa1160d60fd7d8a58caa73e7184bcf6

"""

"""

Set C Test Cases:

9999984630  -- 618 seconds -- 10.31 mins -- c65ae8e178575337c340a501c09e0f3fc5410d2f

1234573350  --  71 seconds  --  ea5eec7aa4cbc9a8ae54fd24a4c7ab26b39fc82a

7653013937  --  494 seconds  --  8.24 mins  --  6e72cda843dc64e1fe5b49243eeb1d6d1ec71509

9943026227  --  625 seconds  --  10.42 mins  --  c09108cc36c9de18012a1db7c88657ac5636b768

"""
