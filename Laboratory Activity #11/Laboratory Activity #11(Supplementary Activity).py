from tkinter import *
import math

window = Tk()
window.title("Calculator with Trigonometric Functions")
window.geometry("600x600")
window.configure(bg="Lightblue")




def press(num):
    entry_var.set(entry_var.get() + str(num))

def evaluate():
    try:
        result= str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Invalid Input.")

def clear():
    entry_var.set("")

def apply_trig(func):
    try:
        result = str(func(math.radians(float(entry_var.get()))))
        entry_var.set(result)
    except:
        entry_var.set("Invalid Input.")





entry_var= StringVar()
entry= Entry(window, textvariable=entry_var, font=("Times New Roman" ,22), justify='right', background="Gold", bd=10)
entry.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=8)

buttons= [
    ('1',2,0), ('2',2,1), ('3',2,2), ('4',2,3), ('cosine',2,4), ("+",2,5),
    ('5',3,0), ('6',3,1), ('7',3,2), ('8',3,3), ('sine',3,4),   ("-",3,5),
    ('9',4,0), ('0',4,1), ('11',4,2), ('12',4,3), ('e^x',4,4), ("*",4,5),
    ('13',5,0), ('14',5,1), ('15',5,2), ('16',5,3), ('**',5,4), ("/",5,5),
]

special_functions = {
    "cosine": lambda: apply_trig(math.cos),
    "sine": lambda: apply_trig(math.sin),
    "e^x": lambda: entry_var.set(str(math.exp(float(entry_var.get()))))
}


for (text, row, col) in buttons:
    if text in special_functions:
        btn = Button(window, text=text, font=("Times New Roman", 22), command=special_functions[text])
    elif text == "=":
        btn = Button(window, text=text, font=("Times New Roman", 22), command=evaluate)
    else:
        btn = Button(window, text=text, font=("Times New Roman", 22), command=lambda t=text: press(t))

    btn.grid(row=row, column=col, ipadx=10, ipady=10, sticky="nsew")

clear_btn = Button(window, text="C", font=("Times New Roman", 22), command=clear,bd=10,foreground="Blue")
clear_btn.grid(row=1, column=0, columnspan=6, ipadx=10, ipady=10, sticky="nsew")


evaluate= Button(window, text="=", font=("Times New Roman",22), command=evaluate,bd=10,foreground="Green")
evaluate.grid(row=6, column=0, columnspan=6, ipadx= 10, ipady=10, sticky="nsew")




window.mainloop()




