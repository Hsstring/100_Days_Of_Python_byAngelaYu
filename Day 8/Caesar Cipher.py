#Caesar Cipher
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def encrypt(text, shift):
    cipher_text=""
    for letter in text:
        encrypt_position = alphabet.index(letter) + shift
        cipher_text += alphabet[encrypt_position]

    print(f"The encoded text is '{ cipher_text}'")
        
def decode(text, shift):
    decode_text=""
    for letter in text:
        decode_position = alphabet.index(letter) - shift
        decode_text += alphabet[decode_position]

    print(f"The decoded text is '{decode_text}'")

go_on = "yes"
while go_on=="yes":
    code_type  = input("Type 'encode' to encrypt, type ' decode' to decrypt\n")
    message = input("Type your message: \n"). lower()
    shift = int(input("Type the shift number: \n"))

    if code_type=="encode":
        encrypt(message, shift)
    elif code_type=="decode":
        decode(message, shift)
    else:
        print("try again!")
    
    go_on = input("do you wanna go on again?(yes/no)  ")
