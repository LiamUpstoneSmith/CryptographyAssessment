# Task 1.4 Text Encryption APP using Stream Cipher and Steganography

import random


def generatekey(text):
    # Generate key using Linear Congruential Generator
    m = 2 ** 32
    a = 1664525
    c = 1013904223
    seed = 42
    key = []
    for i in range(len(text)):
        seed = (a * seed + c) % m
        key.append(seed % 256)

    str_key = ''
    for i in key:
        str_key += chr(i)

    return str_key

def encryption():
    # Get user input
    secret = input("Enter the secret: \n")
    text = input("Enter the text: \n")
    print("------------------------------------------")

    key = generatekey(text)

    # Encrypt secret with stream cipher
    encrypted_secret = ""
    for i in range(len(secret)):
        encrypted_secret += chr(ord(secret[i]) ^ ord(key[i]))

    print(encrypted_secret)

    # calls whitespace with text and encrypted secret
    whitespace(text, encrypted_secret)


# Decrypts whitespace steganography
def decrypt_whitespace(ciphertext):

    ciphertext_length = len(ciphertext)
    text = []
    binary_secret = []

    # Create list with each text value
    for letter in ciphertext:
        text.append(letter)

    i = 0

    # checks if spaces are value 1 or 0 in binary
    while i != ciphertext_length - 1:
        try:
            if text[i] == " " and text[i+1] == " " and text[i+2] == " ":  # if value is 3 spaces
                del (text[i + 1])  # Deletes secret spaces
                del (text[i + 1])  # Deletes secret spaces
                binary_secret.append("1")

            elif text[i] == " " and text[i+1] == " ":  # if value is 2 spaces
                del (text[i+1])  # Deletes secret spaces
                binary_secret.append("0")
        except IndexError:
            break

        # Increase i increment
        i += 1

    # Converts binary_secret from list to string
    binary_secret = ''.join(binary_secret)

    # Convert binary back to string
    streamed_secret = ''.join([chr(int(binary_secret[i:i+8], 2)) for i in range(0, len(binary_secret), 8)])

    # Generates pseudo random key
    key = generatekey(text)

    # Decrypts stream ciphered text
    secret = ""
    for i in range(len(streamed_secret)):
        secret += chr(ord(streamed_secret[i]) ^ ord(key[i]))

    text = ''.join(text)

    # Prints out decrypted values
    print("\nOriginal Text:")
    print(text)
    print("\nSecret:")
    print(secret)


def whitespace(text, secret):
    # Convert Secret to Binary string
    binary_secret = ''.join([format(ord(x), '08b') for x in secret])
    print("Binary Secret: ", binary_secret)

    ciphertext = []
    text_length = len(text)

    i = 0
    position = 0

    # Create list with each text value
    for letter in text:
        ciphertext.append(letter)

    # Change space value based on binary value of secret message
    while i != text_length - 1:
        try:
            if ciphertext[i] == " " and binary_secret[position] == "1":
                ciphertext[i] = "   "  # Replace space with 3 spaces indicating binary value 1
                position += 1

            elif ciphertext[i] == " " and binary_secret[position] == "0":
                ciphertext[i] = "  "  # Replace space with 2 spaces indicating binary value 0
                position += 1
        except IndexError:
            break

        i += 1

    # Make ciphertext a string
    ciphertext = ''.join(ciphertext)

    # Print out values
    print("\nCiphertext:")
    print(ciphertext)
    print("------------------------------------------")

    # Calls Decrypt_whitespace function
    decrypt_whitespace(ciphertext)


encryption()
