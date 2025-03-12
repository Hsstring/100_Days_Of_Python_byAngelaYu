import random
print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many sumbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols = ["!","@","#","$","%","^","&","*"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

password = ""
for n in range(0,n_letters):
    password += random.choice(letters)
for n in range(0,n_symbols):
    password += random.choice(symbols)
for n in range(0,n_numbers):
    password += random.choice(numbers)

pass_letters = list(password)
random.shuffle(pass_letters)
new_password = ""
for ele in pass_letters:
    new_password += ele
print(f"Here is your password:{new_password}")