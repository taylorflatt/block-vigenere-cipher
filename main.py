"""Encrypts text using an iterative block version of the Vigenere Cipher"""
# Created by Taylor Flatt in Python 3.6

TABULA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,.-_'


def encrypt(text, key):
    """Encrypts a block of text using a key."""

    cipher = ""
    for i, j in zip(text, key):
        text_pos = TABULA.index(i)
        key_pos = TABULA.index(j)
        cipher_pos = (text_pos + key_pos) % 30
        cipher += TABULA[cipher_pos]

    return cipher


def main():
    """Prompts the user for some text and a key. Then passes their text
    through the encryption method iteratively until it is completely encrypted."""

    plaintext = input('Enter some text to encrypt: ')
    key = input('Enter a key (some text): ')

    # Break the cipher into blocks relative to the key length.
    blocks = []
    blocks.insert(0, key)
    i = 0
    j = len(key)
    iterations = (len(plaintext) // len(key)) + 1

    # Iterate for as many blocks are necessary for the plaintext input.
    for index in range(0, iterations):
        blocks.append(
            encrypt(plaintext[i:j].upper(), blocks[index][:j - i].upper()))
        i += len(key)

        # Catches blocks smaller than the key.
        if j + len(key) > len(plaintext) - 1:
            j = len(plaintext)
        else:
            j += len(key)

    blocks_joined = ''.join(blocks)

    print("Plaintext: ", plaintext)
    print("Key: ", blocks_joined[:-len(key)])
    print("Ciphertext: ", blocks_joined[len(key):])

if __name__ == "__main__":
    main()
