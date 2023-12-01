# Task 1.3  - Brute Force Password Cracking

import string
import itertools
import hashlib as hash


# SHA1 hashes given input
def crypto_hash(thing):
    hasher = hash.sha1(thing.encode())
    c = hasher.hexdigest()
    return c


# user input hashed password to crack
check = input("\nEnter hashed password:\n")


def set_a(check):

    fire_up_the_jugg = 0

    # Check if password is 1 character long
    for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=1):
        c = ''.join(combination)
        print(c)
        c = crypto_hash(c)
        if c == check:
            print("-------------------------------\n" + str(combination) + "\n-------------------------------")
            fire_up_the_jugg = 0
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
                break
            else:
                print("-------------------------------\n" + "Error no password found" + "\n-------------------------------")
                break


set_a(check)
