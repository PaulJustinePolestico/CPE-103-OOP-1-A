from tkinter import *

window = Tk()
window.title("Using Grid Manager")
window.geometry("800x400")


yscroll = Scrollbar(window,orient= VERTICAL)
yscroll.pack(side=RIGHT ,fill=Y)

listbox = Listbox(window,yscrollcommand=yscroll.set)
listbox.pack(side=RIGHT,fill=BOTH, expand=True)


for x in range(51):
    listbox.insert(END,x)


listbox.config(yscrollcommand=yscroll.set)
yscroll.config(command=listbox.yview)
window.mainloop()