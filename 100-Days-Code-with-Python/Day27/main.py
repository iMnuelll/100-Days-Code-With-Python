from tkinter import *

#Button
def button_clicked() :
  my_label.config(text=input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=1000, height=500)
window.config(padx=100, pady=50)

#Label
my_label = Label(text="I Am a Label", font=("TImes New Roman", 12, "bold"))

# Change or Update the components
# my_label['text'] = "New Text" -> First Method
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

#Input

input = Entry(width=20)
input.grid(column=3, row=2)
input.get()


window.mainloop()