from re import split
from caesar_cipher.corpus_loader import word_list, name_list

def encrypt(plain, key):

    encrypted = ""

    for char in plain:
        if (char.isalpha()):
            if (char.isupper()):
                encrypted += chr(((ord(char) + key - 65) % 26) + 65)
            else:
                encrypted += chr(((ord(char) + key - 97) % 26) + 97)
        else:
            encrypted += char

    return encrypted.lower()

def decrypt(plain, key):
    return encrypt(plain, -key)

def crack(text):
    encrypted_possibilities = []
    
    for shift in range(0,26):
        possible = decrypt(text, shift)
        split_words = possible.split()
        print(split_words)
        for word in split_words:
            if (word in word_list) or (word in name_list):
                encrypted_possibilities.append(word)
    
    return encrypted_possibilities
