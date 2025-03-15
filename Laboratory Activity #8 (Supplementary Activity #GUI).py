import tkinter as tk

#Functions for calculation
def add():
    result.set(float(entry1.get())+float(entry2.get()))

def subtract():
    result.set(float(entry1.get())-float(entry2.get()))

def multiply():
    result.set(float(entry1.get())*float(entry2.get()))

def divide():
    try:
        result.set(float(entry1.get())/float(entry2.get()))
    except ZeroDivisionError:
        result.set("Error! Division by zero.")

def clear():
    result.set("Clear")

#Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("800x600+20+20")
root.configure(bg="Light Blue")

#Create StringVar to hold the result
result = tk.StringVar()

#Create the layout
tk.Label(root,text="Enter first number:").grid(row=0, column=0)
entry1= tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root,text="Enter second number:").grid(row=1, column=0)
entry2= tk.Entry(root)
entry2.grid(row=1, column=1)

#Buttons for operations
tk.Button(root,text="Add",command=add, fg="Green",).grid(row=2,column=0)
tk.Button(root,text="Subtract",command=subtract,fg="Green",).grid(row=2,column=1)
tk.Button(root,text="Multiply",command=multiply,fg="Green").grid(row=3,column=0)
tk.Button(root,text="Divide",command=divide,fg="Green").grid(row=3,column=1)
tk.Button(root,text="Clear",command=clear,fg="Black").grid(row=5, column=1)


#Label to show result
tk.Label(root,text="Result.").grid(row=4, column=0)
result_label=tk.Label(root, textvariable=result)
result_label.grid(row=4, column=1)

#Start the main loop
root.mainloop()
























