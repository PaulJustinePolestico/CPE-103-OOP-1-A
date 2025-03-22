import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Combobox')
window.geometry('1000x500')
window.iconbitmap('user_avatar_people_man_person_icon_262044.ico')


def choice(event):
    month = event.widget.get()
    print("Your birth month", month)

def choice2(event):
    date = event.widget.get()
    print("Your birth date", date)

def choice3(event):
    year = event.widget.get()
    print("Your birth year", year)

def display_birthday():
    month_selected = n.get()
    date_selected = n2.get()
    year_selected = n3.get()
    showinfo(title="Your Birthday", message=f'Your birthday is {month_selected} {date_selected}, {year_selected}')



# label text for title
ttk.Label(window, text="Choose your birth month",
          background='light yellow', foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=1)

# Set label
ttk.Label(window, text="Select the month of your birth :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=5, padx=5, pady=25)

ttk.Label(window, text="Select your birth date :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=6, padx=0, pady=25)

ttk.Label(window, text="Select your birth year :",
          font=("Times New Roman",12)).grid(column=0,
                                            row=7, padx=0, pady=25)

# Create Combobox
n = tk.StringVar()
n2 = tk.StringVar()
n3 = tk.StringVar()
month = ttk.Combobox(window, width=27, textvariable=n)
date  = ttk.Combobox(window, width=27, textvariable=n2)
year = ttk.Combobox(window, width=27, textvariable=n3)



# Adding combobox drop down list
month['values'] = (' January',
                     ' February',
                     ' March',
                     ' April',
                     ' May',
                     ' June',
                     ' July',
                     ' August',
                     'September',
                     'October',
                     'November',
                     'December')

date['values'] = (' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9',' 10', ' 11',' 12',
                  ' 13',' 14',' 15',' 16',' 17',' 18',' 19',' 20',' 21',' 22',' 23',' 24',
                  ' 25',' 26',' 27',' 28',' 29',' 30',' 31')

year['values'] = (' 2005', '2006',' 2007',' 2008',' 2009',' 2010')







month.grid(column=1, row=5)
month.current()

date.grid(column=1, row=6)
date.current()

year.grid(column=1, row=7)
year.current

def choice(event):
    showinfo(
            title = "Selection",
            message = f'You selected{n.get()}')

def choice2(event):
    showinfo(
            title= "Selection",
            message= f'You selected{n2.get()}')

def choice3(event):
    showinfo(
            title= "Selection",
            message= f'You selected{n3.get()}')



month.bind("<<ComboboxSelected>>", choice)
date.bind("<<ComboboxSelected>>", choice2)
year.bind("<<ComboboxSelected>>", choice3)

birthday_button = tk.Button(window, text="Show My Birthday",background="Grey",foreground="Gold", command=display_birthday)
birthday_button.grid(row=8, column=1, pady=20)


window.mainloop()