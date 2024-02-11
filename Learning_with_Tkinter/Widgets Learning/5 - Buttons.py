import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

#button
def button_func():
    print('a basic button')
    print(radiovar.get())

button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(window, text = 'A simple button', command= button_func, textvariable= button_string)     # instead of having to write master, you can just pass the argument for master by just writing it)
button.pack()

# checkbutton

check_var = tk.IntVar(value = 10)     #Sets the initial state of the checkbox to be selected
check1 = ttk.Checkbutton(               #Checkboxes can have multiple values stored within them, and are not connected
    window,
    text = 'checkbox 1',
    command= lambda: print(check_var.get()),
    variable= check_var,
    onvalue= 10,          # sets the value of the checkbox when selected to be 10
    offvalue= 5           # sets the value of the checkbox when unselected to be 5
    )
check1.pack()

check2 = ttk.Checkbutton(
    window,
    text = 'checkbox 2',
    command = lambda: check_var.set(5)
)
check2.pack()

#radio buttons
radiovar = tk.StringVar()
radio1 = ttk.Radiobutton(                  # Radio buttons only have one value for each button and always connected
    window, 
    text = 'radio button 1', 
    value= 'radio 1', 
    variable= radiovar,
    command = lambda: print(radiovar.get())
    )  #When making radio buttons, set a value for each one or else they would have the same value and would have the same function
radio1.pack()

radio2 = ttk.Radiobutton(window, text = 'radio button 2', value= '2', variable = radiovar)
radio2.pack()

#exercise area
ex_check_var = tk.BooleanVar()

# check button
ex_check = ttk.Checkbutton(
    window,
    text = 'exercise checkbutton',
    command= lambda: print(exradio_var.get())  ,
    variable= ex_check_var,
)
ex_check.pack()

# radio buttons
exradio_var = tk.StringVar()
def radio_func():
    print(ex_check_var.get())
    ex_check_var.set(False)

exradio1 = ttk.Radiobutton(
    window,
    text = 'exercise radiobutton',
    value = 'A' ,
    variable= exradio_var,
    command = radio_func)
exradio1.pack()

exradio2 = ttk.Radiobutton(
    window,
    text = 'exercise radiobutton',
    value = 'B' ,
    variable=  exradio_var,
    command = radio_func)
exradio2.pack()

# run
window.mainloop()