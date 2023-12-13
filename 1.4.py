# Task 1.4 Text Encryption APP using Stream Cipher and Steganography

def main():
    # Get user input
    secret = input("Enter the secret: \n")
    text = input("Enter the text: \n")
    print("------------------------------------------")

    key = generate_key(text)

    # Encrypt secret with stream cipher
    encrypted_secret = ""
    for i in range(len(secret)):
        encrypted_secret += chr(ord(secret[i]) ^ ord(key[i]))  # XOR each bit

    choose(text, encrypted_secret)


def choose(text, encrypted_secret):

    # Choose which kind of steganography to encrypt the data.
    choice = input("\nWhat kind of hashing?\nA - Whitespace\nB - Punctuation\n")

    if choice == "A" or choice == "a":
        whitespace(text, encrypted_secret)
    elif choice == "B" or choice == "b":
        punc(text, encrypted_secret)
    else:
        print("Invalid choice")
        choose(text, encrypted_secret)


def generate_key(text):
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
    key = generate_key(text)

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


# Hides Secret Message inside Text, Using whitespace steganography
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


def punc(text, secret):

    # Convert Secret to Binary string
    binary_secret = ''.join([format(ord(x), '08b') for x in secret])
    print("Binary Secret: ", binary_secret)
    print(len(binary_secret))

    punctuation = [",", ".", "'", "#", "~", "/", "?", ">", "<", ";", ":", "'", '"', "@", "[", "{", "]", "}", "_", "-", ")", "(", "*", "&", "!"]

    ciphertext = []
    text_length = len(text)
    print(text_length)

    # Deletes all punctuation already in text
    text_temp = []
    for letter in text:
        text_temp.append(letter)
    for i in range(text_length):
        try:
            if text_temp[i] in punctuation:
                del text_temp[i]
        except IndexError:
            break
    text = ''.join(text_temp)

    # Calculates position_move variable
    # Adds data each at this position
    position_move = len(text) / (len(binary_secret) / 4)
    position_move = position_move // 1  # Rounds float down
    position_move = int(position_move)

    j = 0
    i = 0
    position = 0

    # Create list with each text value
    for letter in text:
        ciphertext.append(letter)

    while j != text_length - 1:
        try:
            if (binary_secret[position] == "1" and binary_secret[position + 1] == "1" and
                    binary_secret[position + 2] == "1" and binary_secret[position + 3] == "1"):  # 1111 = ,
                ciphertext[i] += ","
            elif (binary_secret[position] == "1" and binary_secret[position + 1] == "1" and
                  binary_secret[position + 2] == "1" and binary_secret[position + 3] == "0"):  # 1110 = .
                ciphertext[i] += "."
            elif (binary_secret[position] == "1" and binary_secret[position + 1] == "1" and
                  binary_secret[position + 2] == "0" and binary_secret[position + 3] == "0"):  # 1100 = '
                ciphertext[i] += "'"

            elif (binary_secret[position] == "1" and binary_secret[position + 1] == "0" and
                  binary_secret[position + 2] == "0" and binary_secret[position + 3] == "0"):  # 1000 = #
                ciphertext[i] += "#"

            elif (binary_secret[position] == "0" and binary_secret[position + 1] == "0" and
                  binary_secret[position + 2] == "0" and binary_secret[position + 3] == "0"):  # 0000 = ~
                ciphertext[i] += "~"
                print("Todger")
            elif (binary_secret[position] == "0" and binary_secret[position + 1] == "0" and
                  binary_secret[position + 2] == "0" and binary_secret[position + 3] == "1"):  # 0001 = /
                ciphertext[i] += "/"
                print("Elbow")
            elif (binary_secret[position] == "0" and binary_secret[position + 1] == "0" and
                  binary_secret[position + 2] == "1" and binary_secret[position + 3] == "1"):  # 0011 = ?
                ciphertext[i] += "?"
                print("King")
            elif (binary_secret[position] == "0" and binary_secret[position + 1] == "1" and
                  binary_secret[position + 2] == "1" and binary_secret[position + 3] == "1"):  # 0111 = >
                ciphertext[i] += ">"
                print("Liam")
            elif (binary_secret[position] == "0" and binary_secret[position + 1] == "1" and
                  binary_secret[position + 2] == "1" and binary_secret[position + 3] == "0"):  # 0110 = <
                ciphertext[i] += "<"
                print("Jack")
            elif (binary_secret[position] == "0" and binary_secret[position + 1] == "1" and
                  binary_secret[position + 2] == "0" and binary_secret[position + 3] == "0"):  # 0100 = ;
                ciphertext[i] += ";"
                print("OOKa")
            elif (binary_secret[position] == "0" and binary_secret[position + 1] == "0" and
                  binary_secret[position + 2] == "1" and binary_secret[position + 3] == "0"):  # 0010 = :
                ciphertext[i] += ":"
                print("Johnathon")
            print(i)
        except IndexError:
            break

        i += position_move
        j += 1
        position += 4

    # Make ciphertext a string
    ciphertext = ''.join(ciphertext)

    # Print out values
    print("\nCiphertext:")
    print(ciphertext)
    print("------------------------------------------")

    decrypt_punc(ciphertext)


def decrypt_punc(ciphertext):
    ciphertext_length = len(ciphertext)
    text = []
    binary_secret = []

    # Create list with each text value
    for letter in ciphertext:
        text.append(letter)

    i = 0

    while i != ciphertext_length - 1:
        try:
            if text[i] == ",":
                binary_secret.append("1111")
                del text[i]
            elif text[i] == ".":
                binary_secret.append("1110")
                del text[i]
            elif text[i] == "'":
                binary_secret.append("1100")
                del text[i]
            elif text[i] == "#":
                binary_secret.append("1000")
                del text[i]
            elif text[i] == "~":
                binary_secret.append("0000")
                del text[i]
            elif text[i] == "/":
                binary_secret.append("0001")
                del text[i]
            elif text[i] == "?":
                binary_secret.append("0011")
                del text[i]
            elif text[i] == ">":
                binary_secret.append("0111")
                del text[i]
            elif text[i] == "<":
                binary_secret.append("0110")
                del text[i]
            elif text[i] == ";":
                binary_secret.append("0100")
                del text[i]
            elif text[i] == ":":
                binary_secret.append("0010")
                del text[i]

            i += 1
        except IndexError:
            break

    # Converts binary_secret from list to string
    binary_secret = ''.join(binary_secret)

    # Convert binary back to string
    streamed_secret = ''.join([chr(int(binary_secret[i:i+8], 2)) for i in range(0, len(binary_secret), 8)])

    # Generates pseudo random key
    key = generate_key(text)

    # Decrypts stream ciphered text
    secret = ""
    for i in range(len(streamed_secret)):
        secret += chr(ord(streamed_secret[i]) ^ ord(key[i]))

    text = ''.join(ciphertext)

    # Prints out decrypted values
    print("\nOriginal Text:")
    print(text)
    print("\nSecret:")
    print(secret)


main()
