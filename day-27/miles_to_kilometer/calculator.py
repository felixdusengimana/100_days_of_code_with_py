import tkinter


def convert_to_km():
    miles = float(my_input.get())
    km = miles * 1.609
    my_input1.config(text=f"{km}")
    print("CLicked")

window = tkinter.Tk()

window.minsize(width=300, height=500)
# window.title(text="Mile to Kilometer Converter")

my_input = tkinter.Entry(width=7)
my_input.grid(column=1, row=0)

my_label = tkinter.Label(text="Miles")
my_label.grid(column=2, row=0)

my_label2 = tkinter.Label(text="Is equal")
my_label2.grid(column=0, row=1)

my_input1 = tkinter.Label()
my_input1.grid(column=1, row=1)

my_label3 = tkinter.Label(text="Km")
my_label3.grid(column=2, row=1)

my_button = tkinter.Button(text="Convert", command=convert_to_km)
my_button.grid(column=1, row=3)
window.mainloop()
