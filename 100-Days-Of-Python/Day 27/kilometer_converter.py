from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

kilometers_label = Label(text="0")
kilometers_label.grid(column=1, row=1)

km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)

def convert_miles_to_km():
    miles = float(miles_input.get())
    kilometers = miles * 1.60934
    kilometers_label.config(text=f"{kilometers:.2f}")
convert_button = Button(text="Convert", command=convert_miles_to_km)
convert_button.grid(column=1, row=2)
window.mainloop()


