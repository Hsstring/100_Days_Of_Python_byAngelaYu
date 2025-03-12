#Add
def add(n1,n2):
    return n1+n2

#Subtract
def sub(n1,n2):
    return n1-n2

#Multiply
def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return round(n1/n2,2)
import logo 
print(logo.logo)
operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
def calculator():
    to_continue = "y"
    num1 = float(input("What's the first number? "))
    while to_continue=="y":
        for op in operations:
            print(op, end=" , ")
        operation = input("\nPick an operation from the line above: ")
        num2 = float(input("What's the next number? "))
        
        calculate = operations[operation]
        answer = calculate(num1,num2)

        print(f"{num1} {operation} {num2} = {round(answer,2)}")
        to_continue = input("Type 'y' to continue calculating with 8, or type 'start' to start a new calculation or type 'n' if you're tired of calculating.: ")
        if to_continue=='y':
            num1 = answer
        elif to_continue=="start":
            calculator()
            to_continue = "y"
        else:
            break


calculator()