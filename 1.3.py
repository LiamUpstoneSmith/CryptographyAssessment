# Task 1.3  - Brute Force Password Cracking

import string
import itertools
import hashlib as hash


# Works out ASCII value of string mod length of string
def reduce(thing):
    p = len(thing)
    o = 0

    lst = []

    for letter in thing:
        lst.append(letter)

    for characters in lst:
        o += ord(characters)

    n = o % p
    return n


def crypto_hash(thing):
    hasher = hash.sha1(thing.encode())
    c = hasher.hexdigest()
    return c


# def hashing(check, combinations):
#     start_time = time.time()
#     for w in combinations:
#         c = crypto_hash(w)
#         if str(c) == check:
#             print("-------------------------------\n"+w+"\n-------------------------------")
#             break
#         print(w)
#     else:
#         print(w)
#
#     end_time = time.time()
#     runtime = round(end_time - start_time, 2)
#     print("\n", runtime, " Seconds\n")


# Creating all possible combinations of alphabet up to length of 6
# letters = string.digits + string.ascii_uppercase
# combinations = []
# for i in range(1, 6):
#     combinations.extend([''.join(c) for c in itertools.product(letters, repeat=i)])

# user input hashed password to crack
check = input("\nEnter hashed password:\n")


# def bruteforce(check, combinations):
#     for w in combinations:
#         for i in range(1, 7):  # Checks 6 links into the chain
#             c = crypto_hash(w)
#             if c == check:
#                 print("-------------------------------\n" + w + "\n-------------------------------")
#                 break
#             else:
#                 c = reduce(c)
#                 if c == check:
#                     print("-------------------------------\n" + w + "\n-------------------------------")
#                     break
#         else:
#             continue
#         break


#bruteforce(check, combinations)

def okay(check):
    for combination in itertools.product('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=6):
        for w in range(1,7):
            c = ''.join(combination)
            c = crypto_hash(c)
            if c == check:
                print("-------------------------------\n" + combination + "\n-------------------------------")
                break
            else:
                c = reduce(c)
                if c == check:
                    print("-------------------------------\n" + combination + "\n-------------------------------")
                    break
            print(w)
        else:
            continue
        break


okay(check)

"""

To-Do:
Don't think Reduce function is correct

"""
