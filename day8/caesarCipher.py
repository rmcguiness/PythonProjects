alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
        index = alphabet.index(letter)
        encoded_msg += shift_alph[index]
    return(encoded_msg)

def decrypt(code, shift):
    decoded_msg = ''
    shift_alph = alphabet_shift(shift)
    for letter in code:
        index = shift_alph.index(letter)
        decoded_msg += alphabet[index]
    return(decoded_msg)
    
decoding = True
while decoding:
    continue_decoding = input('Do you want to continue? y/n \n')
    if continue_decoding == "n":
        decoding = False
        break
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        print(encrypt(text, shift))
    elif direction == 'decode':
        print(decrypt(text, shift))
    else:
        print('direction not specified')
