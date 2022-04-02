import string


def main():
    print("Caesar Cipher\n=============")
    shift = 3
    guess = 0

    # Encrpytion
    message = input("Enter your message: ")
    print("Encrypting message now...")
    cipher = encrypt(message.lower(), shift)

    # Decryption
    print("Decrypting message now...")
    while guess < 26:
        decrypt(cipher, guess)
        guess += 1


def encrypt(m: string, s: int):
    """Encrypts the message by shifting the characters forward based on s

    Args:
        m (string): Plaintext
        s (int): Shift number

    Returns:
        c (string): Ciphertext
    """
    c: string = ""
    for character in m:
        character = chr((ord(character) + s - 97) % 26 + 97)
        c += character
    print("Ciphertext: " + c)
    return c


def decrypt(c: string, s: int):
    """Decrypts the ciphertext by shifting the characters back based on s and printing the decoded message

    Args:
        c (string): Ciphertext
        s (int): Shift number
    """
    d: string = ""
    for character in c:
        character = chr((ord(character) - s - 97) % 26 + 97)
        d += character
    print("Decoded Message [" + str(s) + "]: " + d)


if __name__ == "__main__":
    main()
