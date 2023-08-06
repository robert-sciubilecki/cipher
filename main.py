alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(message, shift_setting):

    encrypted_message = ''

    for letter in message:
        if letter not in alphabet:
            encrypted_message += letter
        elif alphabet.index(letter) + shift_setting >= len(alphabet):
            # if the index of encoded character is bigger than the last index of alphabet
            # subtract the length of the alphabet from index of character + shift setting to start counting
            # from the beginning
            encrypted_message += alphabet[alphabet.index(letter) + shift_setting - len(alphabet)]
        else:
            encrypted_message += alphabet[alphabet.index(letter) + shift_setting]

    print(encrypted_message)


def decrypt(message, shift_setting):

    decrypted_message = ''

    for letter in message:
        if letter not in alphabet:
            decrypted_message += letter
        elif alphabet.index(letter) - shift_setting < 0:
            # if the index of character - shift setting is smaller than 0 we have to go to the end of the alphabet
            # and continue moving backwards from there
            decrypted_message += alphabet[alphabet.index(letter) + len(alphabet) - shift_setting]
        else:
            decrypted_message += alphabet[alphabet.index(letter) - shift_setting]

    print(decrypted_message)


if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
