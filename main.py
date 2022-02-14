alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encrypted_text = ""
    for char in text:

        # Skip this iteration of the loop if the character is a space
        if char == " ":
            encrypted_text += " "
            continue

        # Applies the shift, and also allowing for large numbers such as 1000 to be used
        index = alphabet.index(char) + shift
        while index < 0 or index >= 26:
            if index >= 26:
                index -= 26
            if index < 0:
                index += 26
        encrypted_text += alphabet[index]
    print(f"The encrypted message is: {encrypted_text}")


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:

        # Skip this iteration of the loop if the character is a space
        if char == " ":
            decrypted_text += " "
            continue

        # Applies the shift, and also allowing for large numbers such as 1000 to be used
        index = alphabet.index(char) - shift
        while index < 0 or index >= 26:
            if index >= 26:
                index -= 26
            if index < 0:
                index += 26
        decrypted_text += alphabet[index]
    print(f"The decrypted message is: {decrypted_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    if direction == 'decode':
        decrypt(text,shift)

    restart = input("Would you like to go again? (y/n):\n")
    if restart != "yes" and restart != "y":
        print("Goodbye!")
        break
