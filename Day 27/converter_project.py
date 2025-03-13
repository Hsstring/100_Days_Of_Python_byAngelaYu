from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

Miles_label = Label(text="Miles")
Miles_label.grid(column=2, row=0)
Km_label = Label(text="Km")
Km_label.grid(column=2, row=1)
string_label = Label(text="is equal to")
string_label.grid(column=0, row=1)

Miles_entry = Entry(width=8)
Miles_entry.insert(END, string="0")
Miles_entry.grid(column=1, row=0)

kmScale_label = Label(text=0)
kmScale_label.grid(column=1, row=1)


def calculation():
    km = round(int(Miles_entry.get())*1.6)
    kmScale_label["text"] = km


calculate_button = Button(text="Calculate", command=calculation)
calculate_button.grid(column=1, row=2)
window.mainloop()
