import tkinter as tk

#Create the main window
root = tk.Tk()
root.title("Simple Calculator with History")
root.geometry("800x600+20+20")
root.configure(bg="Light Blue")

#Create StringVar to hold the result
result = tk.StringVar()
history = []


#Create the layout
tk.Label(root,text="Enter first number:",bg="Red",fg="Yellow").grid(row=0, column=0)
entry1= tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root,text="Enter second number:",bg="Red",fg="Yellow").grid(row=1, column=0)
entry2= tk.Entry(root)
entry2.grid(row=1, column=1)


#Functions for calculation
def add():
        try:
            value1=float(entry1.get())
            value2=float(entry2.get())
            result_value = value1 + value2
            result.set(result_value)
            history.append(f"{value1} + {value2} = {result_value}")

        except ValueError:
            result.set("You must input a number.")
            history.append("You must input a number.")


def subtract():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        result_value = value1 - value2
        result.set(result_value)
        history.append(f"{value1} - {value2} = {result_value}")

    except ValueError:
        result.set("You must input a number.")
        history.append("You must input a number.")

def multiply():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        result_value = value1 * value2
        result.set(result_value)
        history.append(f"{value1} * {value2} = {result_value}")

    except ValueError:
        result.set("You must input a number.")
        history.append("You must input a number.")

def divide():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        result_value = value1 / value2
        result.set(result_value)
        history.append(f"{value1} / {value2} = {result_value}")

    except ZeroDivisionError:
        result.set("Error! Divsion by zero.")
        history.append("Error! Division by zero.")

def power():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        result_value = value1 ** value2
        result.set(result_value)
        history.append(f"{value1} ** {value2} = {result_value}")

    except ValueError:
        result.set("You must enter a number.")
        history.append("You must enter a number.")

def history_display():
    if history:
        result.set("\n".join(history))
    else:
        result.set("No History Available.")



def clear():
    result.set("Clear")






#Buttons for operations
tk.Button(root,text="Add",command=add, fg="Green",).grid(row=3,column=0)
tk.Button(root,text="Subtract",command=subtract,fg="Green",).grid(row=3,column=2)
tk.Button(root,text="Multiply",command=multiply,fg="Green").grid(row=4,column=0)
tk.Button(root,text="Divide",command=divide,fg="Green").grid(row=4,column=2)
tk.Button(root,text="Clear",command=clear,fg="Gold",bg="Black").grid(row=2, column=0)
tk.Button(root,text="Power",command=power,fg="Green").grid(row=5, column=2)

#Button for history
history_button=tk.Button(root,text="History",command=history_display,fg="Gold",bg="Black").grid(row=2, column=2)


#Label to show result
tk.Label(root,text="Result.",bg="Yellow").grid(row=5, column=0)
result_label=tk.Label(root, textvariable=result)

result_label.grid(row=5, column=1)


#Start the main loop
root.mainloop()
























