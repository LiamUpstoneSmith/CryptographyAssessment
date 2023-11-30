# Task 1.3  - Brute Force Password Cracking

import string
import itertools
import hashlib as hash
import time


# def myhash(hashes):
#     # Hash password using sha1
#     hash_object = hash.sha1(hashes.encode())
#
#     # Convert hash value to an integer using modulo arithmetic
#     hash_int = int.from_bytes(hash_object.digest(), byteorder='big') % (10 ** 8)
#
#     return hash_int

def reduce(thing):
    pass


def crypto_hash(thing):
    hasher = hash.sha1(thing.encode())
    c = hasher.hexdigest()
    return c


def hashing(check, combinations):
    start_time = time.time()
    for w in combinations:
        for i in range(1, 7):
            c = crypto_hash(w)
            if str(c) == check:
                print("-------------------------------\n"+w+"\n-------------------------------")
                break
            print(w)
        else:
            print(w)
            continue
        break
    end_time = time.time()
    runtime = round(end_time - start_time, 2)
    print("\n",runtime , " Seconds\n")


# Creating all possible combinations of alphabet up to length of 6
letters = string.ascii_uppercase + string.digits
combinations = []
for i in range(1, 7):
    combinations.extend([''.join(c) for c in itertools.product(letters, repeat=i)])


# user input hashed password to crack
#check = input("\nEnter hashed password:\n")


#hashing(check, combinations)

print(combinations[-1])