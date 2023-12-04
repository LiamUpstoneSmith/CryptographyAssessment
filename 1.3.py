# Task 1.3  - Brute Force Password Cracking

"""

Set A Test Cases:

MAKE  --  1029 seconds  --  17.16 mins  --  5f4395a75c71fe04b6156d6290da65a27f17e138

1YOUR1  --  49523 seconds  --  825.4 mins  --  13.75 hours  --  16607928013478be20d30ccd60d958149bd48541

PWD5  --  1268 seconds  --  21.14 mins  --  74fcb3939fb7460f1e6a00a32ca45510ebff9ffa

LONGER  --  75734 seconds  --  1262 mins --  21.03 hours  --  88765f800a890eef93767f976eca17f91cbf85ea

4 --  6.51  --  1b6453892473a467d07372d45eb05abc2031647a

BETTER  --  70725 seconds  --  1178.76 mins  --  19.65 hours  --  3bb9cdac38c5c43cd6cbe4752c40041d58894545

SECRET  --  75187 seconds  --  1253.13 mins  --  20.89 hours  --  3c3b274d119ff5a5ec6c1e215c1cb794d9973ac1  THE PC CODE RUNNING

"""

import itertools
import hashlib as hash
import time

# Starts timer
start_time = time.time()


# SHA1 hashes given input
def crypto_hash(thing):
    hasher = hash.sha1(thing.encode())
    c = hasher.hexdigest()
    return c


# user input hashed password to crack
hashed_password = input("\nEnter hashed password:\n")


def set_a(check):

    num_letters = 0

    # Check if password is 1 character long
    for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=1):
        c = ''.join(combination)
        print(c)
        c = crypto_hash(c)
        if c == check:
            answer = ''.join(combination)
            print("-------------------------------\n" + answer + "\n-------------------------------")
            num_letters = 0
            end_time = time.time()
            break
        else:
            for i in range(1000):  # Hashes combination to 1000th level
                c = crypto_hash(c)
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
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
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
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
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
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
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
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
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
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                num_letters = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        num_letters = 0
                        end_time = time.time()
                        break
                    else:
                        num_letters = 0
                        break

    # Calculates and prints time taken for algorithm to complete
    overall_secs = end_time - start_time
    overall_mins = overall_secs / 60
    overall_secs = round(overall_secs, 2)
    overall_mins = round(overall_mins, 2)
    print("\n", overall_secs, " Seconds to complete")
    print("\n", overall_mins, " mins to complete")


set_a(hashed_password)
