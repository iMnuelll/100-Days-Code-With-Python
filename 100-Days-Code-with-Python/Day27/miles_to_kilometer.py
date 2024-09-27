from tkinter import *

FONT = ("Arial", 12, "bold")

# Button Clicked
def button_clicked() :
  miles = float(input.get())
  kilometers = miles * 1.60934
  answer.config(text=int(kilometers))

# Window
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)

# Label
miles_text = Label(text="Miles", font=FONT)
miles_text.grid(column=4, row=0)

is_equal_to = Label(text="Is Equal To", font=FONT)
is_equal_to.grid(column=0, row=1)

answer  = Label(text=0, font=FONT)
answer.grid(column=2, row=1)

kiloMeter = Label(text="KM", font=FONT)
kiloMeter.grid(column=4, row=1)

# Input
input = Entry(width=10)
input.grid(column=2, row=0)

# Button
calculateButton = Button(text="Calculate", font=FONT, command = button_clicked)
calculateButton.grid(column=2, row=2)

window.mainloop()