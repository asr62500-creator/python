import customtkinter as ctk

# Setup window
ctk.set_appearance_mode("dark")     # "light" or "dark"
ctk.set_default_color_theme("blue") # "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("350x480")
app.resizable(False, False)

# Entry field
entry = ctk.CTkEntry(app, width=320, height=60, corner_radius=15, font=("Arial", 22))
entry.place(x=15, y=20)

# Functions
def click(value):
    entry.insert("end", value)

def clear():
    entry.delete(0, "end")

def equal(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert(0, str(result))
    except:
        entry.delete(0, "end")
        entry.insert(0, "Error")

def backspace(event=None):
    text = entry.get()
    entry.delete(0, "end")
    entry.insert(0, text[:-1])

# Keyboard bindings
app.bind("<Return>", equal)
app.bind("<BackSpace>", backspace)

# Button layout
buttons = [
    ("7", 100, 120), ("8", 150, 120), ("9", 200, 120), ("/", 250, 120),
    ("4", 100, 180), ("5", 150, 180), ("6", 200, 180), ("*", 250, 180),
    ("1", 100, 240), ("2", 150, 240), ("3", 200, 240), ("-", 250, 240),
    ("0", 100, 300), (".", 150, 300), ("=", 200, 300), ("+", 250, 300),
]

# Create buttons
for (text, x, y) in buttons:
    if text == "=":
        ctk.CTkButton(app, text=text, width=40, height=40, corner_radius=10, command=equal).place(x=x, y=y)
    else:
        ctk.CTkButton(app, text=text, width=40, height=40, corner_radius=10,
                      command=lambda t=text: click(t)).place(x=x, y=y)

# Clear and Backspace buttons
ctk.CTkButton(app, text="C", width=95, height=40, corner_radius=10, command=clear).place(x=100, y=360)
ctk.CTkButton(app, text="⌫", width=95, height=40, corner_radius=10, command=backspace).place(x=205, y=360)

app.mainloop()