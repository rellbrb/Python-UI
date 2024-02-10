import tkinter as tk
from tkinter import ttk

def button_func():                        #defines a function that prints out text when the button is pressed
    print('A button was pressed')  

def exercise_func():
    print('hello') 
    
# create a window
window = tk.Tk()                  # creates a window     
window.title('Window and Widgets')
window.geometry('800x500')         #Sets the original size of the window when opened to be 800 pixels wide and 500 tall

# ttk labeltaht
label = ttk.Label(master = window, text = 'This is a test')      # Creates a label that displays the specified text in the window
label.pack()

# create widgets
text = tk.Text(master = window)        # The master specifies where the widget is going to be (like a parent), and 
text.pack()                       # pack places a widget in the middle on the top and works down as it continuous to be called

# ttk entry
entry = ttk.Entry(master = window)     # initialises a text box that text can be input
entry.pack()

# exercise label and button
exercise_label = ttk.Label(master = window, text= 'my label')
exercise_button = ttk.Button(master= window, text = 'exercise button', command = exercise_func)
exercise_label.pack()
exercise_button.pack()

# ttk button
#button = ttk.Button(master = window, text = 'A button', command = button_func)      # initialises a button that can be pressed DONT CALL command FUNCTION (put brackets next to it)
button = ttk.Button(master = window, text = 'A button', command = lambda: print('hello'))      
button.pack()


# run
window.mainloop()        # mainloop updates the gui, checks for events (button clicks, mouse movement, closing the window) and runs until application is closed
