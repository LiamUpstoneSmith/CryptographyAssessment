# Task 1.4 Text Encryption APP using Stream Cipher and Steganography

import random
import string


def lcg(a=22695477, b=1, p=2**32, seed=100, num_range=None):

    x0 = seed

    x_prev = (a * x0 + b) % p

    return x_prev

    # if num_range is None:
    #     return x_prev
    # else:
    #     return int((x_prev / (p - 1)) * (num_range[1] - num_range[0]) + num_range)



def stream_cipher(message, do_encrypt=True):

    key = str(lcg())

    chars = string.ascii_letters + string.digits + ";:,\'?/|{}[]-=+_!@#$%^&*()<>`~\""

    if do_encrypt:

        binary_message = ""
        binary_key = ""

        for char in message:
            binary_message += format(ord(char), "08b")
        for char in key:
            binary_key += format(ord(char), "08b")

        def xor_binary(a, b):
            return '{0:b}'.format(int(a, 2) ^ int(b, 2)).zfill(max(len(a), len(b)))

        binary_ciphertext = xor_binary(binary_message, binary_key)

        binary_ciphertext = [(binary_ciphertext[i:i+5]) for i in range(0, len(binary_ciphertext), 5)]

        acsii_ciphertext = ""

        for i in range(0, len(binary_ciphertext), 8):
            byte = binary_ciphertext[i:i+8]
            acsii_ciphertext += chr(int(byte, 2))

        print(acsii_ciphertext)



def encryption():

    # User enter message 1
    #message1 = input("Enter Message one")

    # User enter message 2 to be encrypted
    message2 = input("Enter Message two:\n")

    stream_cipher(message2)


encryption()
