#Caesar Cipher
import logo
print(logo.logo)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def caesar(type, text, shift):
    cipher_text="" 
    if type == "decode":
        shift *= -1
    for char in text:
        if char not in alphabet:
            cipher_text += char  
        else: 
            cipher_position= alphabet.index(char) + shift
            cipher_text += alphabet[cipher_position]
    print(f"The {type}d text is '{ cipher_text}'")


go_on = "yes"
while go_on=="yes":
    code_type  = input("Type 'encode' to encrypt, type ' decode' to decrypt\n")
    message = input("Type your message: \n"). lower()
    shift = int(input("Type the shift number: \n"))
    shift = shift % 26
    caesar(code_type, message, shift)
    go_on = input("do you wanna go on again?(yes/no)  ")

print("Byeee")