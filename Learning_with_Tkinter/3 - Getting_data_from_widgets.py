import tkinter as tk
from tkinter import ttk

def button_func():
    #get content of the entry
    entry_text = entry.get()    # saves the input from entry in entry_text 
    
    # update the label
    #label.configure(text = 'weeeeeee')       #Changes the text on the label when the button is pressed
    label['text'] = entry_text                 #Using indexing to change the text is the better method and changes label to whatever is stored in entry_text
    entry['state'] = 'disabled'           #disables the entry widget when the button is pressed
    
def reset_func():
    label['text'] = 'Poop'            # changes text back to poop
    entry['state'] = 'enabled'        #entry widget is re-enabled
    
# window
window = tk.Tk()
window.title('Gettinng and setting widgets')

# widgets
label = ttk.Label(master= window, text = 'Poop')
label.pack()

entry = ttk.Entry(master= window)
entry.pack()

button = ttk.Button(master= window, text=' A button', command = button_func)
button.pack()

exercise_button = ttk.Button(master = window, text = 'Reverse button' , command = reset_func )
exercise_button.pack()

#run
window.mainloop()
print(label.configure())            # returns all the options within label