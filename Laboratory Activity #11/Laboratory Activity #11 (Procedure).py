from tkinter import *
import math

window = Tk()
window.title("Calculator")
window.geometry("800x600")
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
entry= Entry(window, textvariable=entry_var, font=("Times New Roman" ,22), justify='right', background="White", bd=15)
entry.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=8)


#First Row
seven_btn = Button(window, text="7", font=("Times New Roman", 22), command=lambda: press("7"))
seven_btn.grid(row=3, column=0, columnspan=2, ipadx=10, ipady=10, sticky="nsew")

eight_btn = Button(window, text="8", font=("Times New Roman", 22), command=lambda: press("8"))
eight_btn.grid(row=3, column=2, columnspan=1, ipadx=10, ipady=10, sticky="nsew")

nine_btn = Button(window, text="9", font=("Times New Roman", 22), command=lambda: press("9"))
nine_btn.grid(row=3, column=3, columnspan=1, ipadx=10, ipady=10, sticky="nsew")

divide_btn = Button(window, text="/", font=("Times New Roman", 22), command=lambda: press("/"))
divide_btn.grid(row=3, column=4, columnspan=2, ipadx=10, ipady=10, sticky="nsew")



#2nd Row
four_btn = Button(window, text="4", font=("Times New Roman", 22), command=lambda: press("4"))
four_btn.grid(row=4, column=0, columnspan=2, ipadx=10, ipady=10, sticky="nsew")

five_btn = Button(window, text="5", font=("Times New Roman", 22), command=lambda: press("5"))
five_btn.grid(row=4, column=2, columnspan=1, ipadx=10, ipady=10, sticky="nsew")

six_btn = Button(window, text="6", font=("Times New Roman", 22), command=lambda: press("6"))
six_btn.grid(row=4, column=3, columnspan=1, ipadx=10, ipady=10, sticky="nsew")

divide_btn = Button(window, text="*", font=("Times New Roman", 22), command=lambda: press("*"))
divide_btn.grid(row=4, column=4, columnspan=2, ipadx=10, ipady=10, sticky="nsew")



#3rd Row
one_btn = Button(window, text="1", font=("Times New Roman", 22), command=lambda: press("1"))
one_btn.grid(row=5, column=0, columnspan=2, ipadx=10, ipady=10, sticky="nsew")

two_btn = Button(window, text="2", font=("Times New Roman", 22), command=lambda: press("2"))
two_btn.grid(row=5, column=2, columnspan=1, ipadx=10, ipady=10, sticky="nsew")

three_btn = Button(window, text="3", font=("Times New Roman", 22), command=lambda: press("3"))
three_btn.grid(row=5, column=3, columnspan=1, ipadx=10, ipady=10, sticky="nsew")

divide_btn = Button(window, text="-", font=("Times New Roman", 22), command=lambda: press("-"))
divide_btn.grid(row=5, column=4, columnspan=2, ipadx=10, ipady=10, sticky="nsew")




#4rd Row
zero_btn = Button(window, text="0", font=("Times New Roman", 22), command=lambda: press("0"))
zero_btn.grid(row=10, column=0, columnspan=2, ipadx=10, ipady=10, sticky="nsew")


decimal_btn = Button(window, text=".", font=("Times New Roman", 22),command=lambda: press("."))
decimal_btn.grid(row=
              10, column=2, columnspan=2, ipadx=10, ipady=10, sticky="nsew")

add_btn = Button(window, text="+", font=("Times New Roman", 22), command=lambda: press("+"))
add_btn.grid(row=10, column=4, columnspan=6, ipadx=10, ipady=10, sticky="nsew")


#Clear Button (Row 1)
clear_btn = Button(window, text="C", font=("Times New Roman", 22), command=clear)
clear_btn.grid(row=1, column=0, columnspan=6, ipadx=10, ipady=10, sticky="nsew")

#5th (Last) Row
evaluate= Button(window, text="=", font=("Times New Roman",22), command=evaluate)
evaluate.grid(row=11, column=0, columnspan=6, ipadx= 10, ipady=10, sticky="nsew")





window.mainloop()




