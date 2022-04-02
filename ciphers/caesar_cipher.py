import string


def main():
    print('Caesar Cipher\n=================')

    while True:
        # Ask for choice
        choice = input('Do you want to encrypt or decrypt the message? (E/D): ')

        # Encryption
        if choice.capitalize() == 'E':
            message = input('Enter your message: ')
            while True:
                shift = input('Enter number of shifts: ')
                if shift.isnumeric():
                    print('Encrypting message now...')
                    encrypt(message.lower(), int(shift))
                    break
                else:
                    print('That is not a number!')
            break
        # Decryption
        elif choice.capitalize() == 'D':
            guess = 0
            ciphertext = input('Enter your ciphertext: ')
            print('Decrypting message now...')
            while guess < 26:
                decrypt(ciphertext, guess)
                guess += 1
            break
        else:
            print('That is not a valid string!')



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
