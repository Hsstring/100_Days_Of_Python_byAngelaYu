print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10,12, or 15? "))
people = int(input("How many people to split the bill? "))
percentage = percentage*0.01
tip = total_bill*percentage
total_bill = tip + total_bill
pay = total_bill/people
print(f"Each person should pay: {round(pay,2)}")