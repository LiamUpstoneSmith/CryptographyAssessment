# Task 1.3  - Brute Force Password Cracking

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

    fire_up_the_jugg = 0

    # Check if password is 1 character long
    for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=1):
        c = ''.join(combination)
        print(c)
        c = crypto_hash(c)
        if c == check:
            answer = ''.join(combination)
            print("-------------------------------\n" + answer + "\n-------------------------------")
            fire_up_the_jugg = 0
            end_time = time.time()
            break
        else:
            for i in range(1000):  # Hashes combination to 1000th level
                c = crypto_hash(c)
                if c == check:
                    answer = ''.join(combination)
                    print("-------------------------------\n", answer, "Hashed in :", i,
                          "\n-------------------------------")
                    fire_up_the_jugg = 0
                    end_time = time.time()
                    break
                else:
                    fire_up_the_jugg = 1

    # Check if password is 2 characters long
    if fire_up_the_jugg == 1:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=2):
            c = ''.join(combination)
            print(c)
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                fire_up_the_jugg = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        fire_up_the_jugg = 0
                        end_time = time.time()
                        break
                    else:
                        fire_up_the_jugg = 2

    # Check if password is 3 characters long
    if fire_up_the_jugg == 2:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=3):
            c = ''.join(combination)
            print(c)
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                fire_up_the_jugg = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        fire_up_the_jugg = 0
                        end_time = time.time()
                        break
                    else:
                        fire_up_the_jugg = 3

    # Check if password is 4 characters long
    if fire_up_the_jugg == 3:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=4):
            c = ''.join(combination)
            print(c)
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                fire_up_the_jugg = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        fire_up_the_jugg = 0
                        end_time = time.time()
                        break
                    else:
                        fire_up_the_jugg = 4

    # Check if password is 5 characters long
    if fire_up_the_jugg == 4:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=5):
            c = ''.join(combination)
            print(c)
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                fire_up_the_jugg = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        fire_up_the_jugg = 0
                        end_time = time.time()
                        break
                    else:
                        fire_up_the_jugg = 5

    # Check if password is 6 characters long
    if fire_up_the_jugg == 5:
        for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=6):
            c = ''.join(combination)
            print(c)
            c = crypto_hash(c)
            if c == check:
                answer = ''.join(combination)
                print("-------------------------------\n" + answer + "\n-------------------------------")
                fire_up_the_jugg = 0
                end_time = time.time()
                break
            else:
                for i in range(1000):  # Hashes combination to 1000th level
                    c = crypto_hash(c)
                    if c == check:
                        answer = ''.join(combination)
                        print("-------------------------------\n", answer, "Hashed in :", i,
                              "\n-------------------------------")
                        fire_up_the_jugg = 0
                        end_time = time.time()
                        break
                    else:
                        print(
                            "-------------------------------\n" + "Error no password found" +
                            "\n-------------------------------")
                        break

    # Calculates and prints time taken for algorithm to complete
    overall_time = end_time - start_time
    overall_mins = overall_time / 60
    print("\n", overall_time, " Seconds to complete")
    print("\n", overall_mins, " mins to complete")


set_a(hashed_password)
