alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def alphabet_shift(shift):
    shifted_alphabet = alphabet[:]
    for i in range(shift):
        pop = shifted_alphabet.pop(0)
        shifted_alphabet.append(pop)
    return(shifted_alphabet)

def encrypt(text, shift):
    encoded_msg = ''
    shift_alph = alphabet_shift(shift)
    for letter in text:
        for i in range(len(alphabet)):
            if alphabet[i] == letter:
                encoded_msg += shift_alph[i]
    return(encoded_msg)

def decrypt(code, shift):
    decoded_msg = ''
    shift_alph = alphabet_shift(shift)
    for letter in code:
        for i in range(len(shift_alph)):
            if shift_alph[i] == letter:
                decoded_msg += alphabet[i]
    return(decoded_msg)

if direction == 'encode':
    print(encrypt(text, shift))
elif direction == 'decode':
    print(decrypt(text, shift))
