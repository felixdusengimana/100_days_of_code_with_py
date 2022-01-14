import tkinter

window = tkinter.Tk()

window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# Label
my_label = tkinter.Label(text="I am label", font=("Ariel", 24, "bold"))
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)
# Entry

my_input = tkinter.Entry(width=40)
# my_input.pack()
my_input.grid(column=3, row=3)


# Button
def event_function():
    new_text = my_input.get()
    my_label.config(text=new_text)


my_button = tkinter.Button(text="Button 1", command=event_function)
# my_button.config(bg="blue")
# my_button.pack()
my_button.grid(column=1, row=1)
window.mainloop()
