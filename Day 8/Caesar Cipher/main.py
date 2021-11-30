import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    if direction == "encode":
        cipher_text = ""
        text = text.lower()
        if shift > 26:
            shift = shift % 26
        for x in text:
            if x in alphabet:
                ind = int(alphabet.index(x)) + shift
                if ind > 26:
                    ind = ind % 26
                cipher_text += alphabet[ind]
            else:
                cipher_text += x
        print(f"The encoded text is: {cipher_text}")

    elif direction == "decode":
        cipher_text = ""
        text = text.lower()
        if shift > 26:
            shift = shift % 26
        for x in text:
            if x in alphabet:
                ind = int(alphabet.index(x)) - shift
                if ind > 26:
                    ind = ind % 26
                cipher_text += alphabet[ind]
            else:
                cipher_text += x
        print(f"The decoded text is: {cipher_text}")

print(art.logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)

    yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if yes_or_no == "yes":
        continue
    else:
        print("Goodbye")
        break
