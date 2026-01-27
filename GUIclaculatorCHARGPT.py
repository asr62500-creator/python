from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Calculator")

# Entry widget to display the expression
entry = Entry(root, width=20, font=('Arial', 20), borderwidth=5, relief='ridge')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button click
def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + value)

# Function to clear the entry box
def clear():
    entry.delete(0, END)

# Function to evaluate the expression
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

# Create and place the buttons
for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=5, height=2, command=equal).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, width=5, height=2, command=lambda t=text: click(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
Button(root, text="C", width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the GUI loop
root.mainloop()