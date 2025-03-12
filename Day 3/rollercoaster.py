print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
pay =0;
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?"))
    if age<= 12:
        print("Please pay $5.")
        pay =5
    elif age<=18:
        print("Please pay $7")
        pay =7
    else:
        print("Please pay $12.")
        pay =12
    photo = input("Do you want photos?yes/no ")
    if photo =="yes":
        print("You have to pay $3 more")
        pay +=3
    print(f"The total bill is ${pay}")
else:
    print("Sorry, you have to grow taller before you can ride it.")
