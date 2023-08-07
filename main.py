alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(original_text, shift_setting, direction_setting):

    transformed_text = ''

    shift_setting = shift_setting % 26

    for letter in original_text:
        if letter not in alphabet:
            transformed_text += letter

        if direction_setting == 'encode':
            if alphabet.index(letter) + shift_setting >= len(alphabet):
                # if the index of encoded character is bigger than the last index of alphabet
                # subtract the length of the alphabet from index of character + shift setting to start counting
                # from the beginning
                transformed_text += alphabet[alphabet.index(letter) + shift_setting - len(alphabet)]
            else:
                transformed_text += alphabet[alphabet.index(letter) + shift_setting]
        elif direction_setting == 'decode':
            if alphabet.index(letter) - shift_setting < 0:
                # if the index of character - shift setting is smaller than 0 we have to go to the end of the alphabet
                # and continue moving backwards from there
                transformed_text += alphabet[alphabet.index(letter) - shift_setting + len(alphabet)]
            else:
                transformed_text += alphabet[alphabet.index(letter) - shift_setting]
        else:
            print("Make sure to type 'decode' or 'encode' when presented with option to encrypt/decrypt")
            break
    print(f"Your message after transformation: {transformed_text}")


app_on = True

while app_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text, shift, direction)

    again = input("Type 'yes' if you want to go again or 'no' if you want to quit: ").lower()

    if again == 'yes':
        continue
    elif again == 'no':
        app_on = False
