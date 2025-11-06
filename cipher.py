# Dictionary that defines the substitution cipher.
cifra = {
    'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c',
    'f': 'x', 'g': 'z', 'h': 'l', 'i': 'k', 'j': 'j',
    'k': 'h', 'l': 'g', 'm': 'f', 'n': 'd', 'o': 's',
    'p': 'a', 'q': 'q', 'r': 'w', 's': 'e', 't': 'r',
    'u': 't', 'v': 'y', 'w': 'u', 'x': 'i', 'y': 'o',
    'z': 'p'
}

# Reverse mapping used for decryption.
decifra = {valor: chave for chave, valor in cifra.items()}


def encrypt(msg):
    """Encrypts a message using the substitution cipher."""
    return ''.join(cifra.get(c.lower(), c) for c in msg)


def decrypt(msg):
    """Decrypts a message using the reverse substitution dictionary."""
    return ''.join(decifra.get(c.lower(), c) for c in msg)


if __name__ == "__main__":
    while True:
        print("\n--- CIPHER MENU ---")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            msg = input("Message to encrypt: ")
            if not msg:
                print("Error: empty message.")
            else:
                print("Encrypted message:", encrypt(msg))

        elif option == "2":
            msg = input("Message to decrypt: ")
            if not msg:
                print("Error: empty message.")
            else:
                print("Decrypted message:", decrypt(msg))

        elif option == "3":
            print("Program terminated.")
            break

        else:
            print("Invalid option.")
