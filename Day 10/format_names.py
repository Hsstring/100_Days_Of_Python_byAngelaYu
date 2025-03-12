# Functions with Outputs

def format_name(f_name,l_name):
    if f_name==""or l_name=="":
        return "You didn't provide valid input."
        #note that you can use return itself and it returns null and breaks
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name + " " + l_name

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
full_name = format_name(first_name, last_name)
print("Your full name is :  ", full_name)