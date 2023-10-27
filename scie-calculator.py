import tkinter as tk
import math

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = entry.get()
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("sqrt", "math.sqrt")
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "AC":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=20, ipady=20, sticky="nsew")

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "AC", "+",
    "(", ")", "^", "=",
    "sin", "cos", "tan", "√",
    "log", "ln", "π", "e"
]

colors = {
    "numbers": "lightgray",
    "operators": "lightblue",
    "functions": "lightgreen",
    "clear": "red",
    "equals": "orange"
}

row, col = 1, 0
for button_text in buttons:
    color = "lightgray"  # Default color for numeric buttons
    if button_text in "/*-+^()":
        color = "lightblue"  # Operators
    elif button_text in ("sin", "cos", "tan", "√", "log", "ln", "π", "e"):
        color = "lightgreen"  # Functions
    elif button_text == "AC":
        color = "red"  # Clear button
    elif button_text == "=":
        color = "orange"  # Equals button

    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 16), padx=20, pady=20, bg=color)
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make the grid cells expand with window resizing
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
