from tkinter import *

# Create a window
window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# Create a label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.grid(column=0, row=0)  # place it on the screen
my_label["text"] = "New Text"
my_label.config(text="New text", padx=10, pady=10)

# Create an Entry
name = Entry(width=10)
name.grid(column=3, row=2)
print(name.get())


# Create a Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got clicked!")
    print(name.get())
    my_name = Label(text=f"you wrote:{name.get()}")
    my_name.grid(column=1, row=1)


button = Button(text="Click me", command=button_clicked)  # button_clicked is the name of the function
button.grid(column=1, row=1)

new_button = Button(text="Click me", command=button_clicked)
new_button.grid(column=2, row=0)
# Keep the window on the screen
window.mainloop()
