import tkinter as tk


root = tk.Tk()

# None means that we'll create the button later
rows = [
    ['7', '8', '9', '*', '/'],
    ['4', '5', '6', '+', '-'],
    ['1', '2', '3', None, None],
    [None, None, '.', None, None],
]

for y, row in enumerate(rows):
    for x, character in enumerate(row):
        if character is not None:
            button = tk.Button(root, text=character)
            button.grid(row=y, column=x, sticky='nswe')

zerobutton = tk.Button(root, text='0')
zerobutton.grid(row=3, column=0, columnspan=2, sticky='nswe')
equalbutton = tk.Button(root, text='=')
equalbutton.grid(row=2, column=3, rowspan=2, columnspan=2, sticky='nswe')

# let's make everything stretch when the window is resized
for x in range(5):
    root.grid_columnconfigure(x, weight=1)
for y in range(4):
    root.grid_rowconfigure(y, weight=1)

root.title("Calculator")
root.mainloop()
