import tkinter as tk
from tkinter import ttk

def button_func():           # function causes the value written in entry box to be printed and button pressed to becime new label when button is pressed
    print(string_var.get())
    string_var.set('button pressed')   # sets the value of string var

# window
window = tk.Tk()
window.title('Tkinter variable')

#tkinter variable
string_var = tk.StringVar()     # string var allows storage of a string value
string_var1 = tk.StringVar(value= 'test')

# widget
label = ttk.Label(master =window, text = 'label', textvariable= string_var)
label.pack()

entry = ttk.Entry(master= window, textvariable= string_var)  # text variable being string variable allows the label to be changed as entry is changed
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)    
button.pack()


label1 = ttk.Label(master=window, text = 'what', textvariable= string_var1)
label1.pack()
entry_1 = ttk.Entry(master=window, textvariable= string_var1)
entry_1.pack()
entry_2 = ttk.Entry(master=window, textvariable= string_var1)
entry_2.pack()


# run
window.mainloop()