from  tkinter import *

def button_clicked():
    print("I got clicked")
    my_text = input_box.get()
    my_label.config(text=my_text)


window =Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a Label", font=("Arial", 25))
my_label.config(text="Hello World")
my_label.grid(row=0, column=0, pady=10)

#Entry
input_box = Entry(width=30, bd=3)
input_box.grid(row=1, column=0, pady=10)
input_box.focus()

# New Button
new_button = Button(text="New Text")
new_button.grid(row=2, column=0, pady=10)

#Button
button = Button(text="Click me", command= button_clicked)
button.grid(row=3, column=0, pady=10)

window.mainloop()
