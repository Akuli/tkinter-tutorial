import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

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
            # try this without width=3 so you'll know why i put it there
            button = ttk.Button(big_frame, text=character, width=3)
            button.grid(row=y, column=x, sticky='nswe')

# the widths of these buttons are set to smallest possible values because grid
# will make sure that they are wide enough, e.g. zerobutton is below '1' and
# '2', and it will have the same width as the '1' and '2' buttons together
zerobutton = ttk.Button(big_frame, text='0', width=1)
zerobutton.grid(row=3, column=0, columnspan=2, sticky='nswe')
equalbutton = ttk.Button(big_frame, text='=', width=1)
equalbutton.grid(row=2, column=3, rowspan=2, columnspan=2, sticky='nswe')

# let's make everything stretch when the window is resized
for x in range(5):
    big_frame.grid_columnconfigure(x, weight=1)
for y in range(4):
    big_frame.grid_rowconfigure(y, weight=1)

root.title("Calculator")
root.mainloop()
