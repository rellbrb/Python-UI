import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()     # Mile input is set to be the value input in the entry bar
    km_output = mile_input * 1.61    # Formula to converst miles into km
    output_string.set(km_output)     # Shows the value of the mile in km
# window
window = ttk.Window(themename = 'darkly')    # Creates the main window 
window.title('Demo')
window.geometry('300x150')   # initial size of window

# title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()   # Allows label to be placed on window, the pack method allows widgets to be placed bellow each other

# input field
input_frame = ttk.Frame(master = window)  #Creates a frame on the window
entry_int = tk.IntVar() # Stores values entered in entry field  
entry = ttk.Entry(master = input_frame, textvariable = entry_int)  # Initialises a text box on the input frame
button = ttk.Button(master = input_frame, text = 'Convert', command = convert )  # Initialises a button on the input frame
entry.pack(side = 'left', padx = 10)  # Allows entry to be placed on the input frame and on the same line as the button with a space between
button.pack(side = 'left') # Allows button to be placed on the input frame
input_frame.pack(pady = 10)  # Allows input frame to be placed on the window, with extra padding above and below the frame

# output
output_string= tk.StringVar()   # Initializes output string as a string variable/value
output_label = ttk.Label(master = window, 
                         text = 'Output', 
                         font = 'Calibri 24', 
                         textvariable = output_string)   # Initialises an output in the window of the value stored in output string 
output_label.pack(pady = 5)   # Allows output to be shown in the window, with padding/space above and below it

# run
window.mainloop()    # Sjows the window with all the widgets added