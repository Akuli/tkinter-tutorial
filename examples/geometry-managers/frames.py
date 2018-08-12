import tkinter
from tkinter import ttk


def make_calculator_frame(big_frame):
    frame = ttk.Frame(big_frame)

    rows = [
        ['7', '8', '9', '*', '/'],
        ['4', '5', '6', '+', '-'],
        ['1', '2', '3', None, None],
        [None, None, '.', None, None],
    ]

    for y, row in enumerate(rows):
        for x, character in enumerate(row):
            if character is not None:
                button = ttk.Button(frame, text=character, width=3)
                button.grid(row=y, column=x, sticky='nswe')

    zerobutton = ttk.Button(frame, text='0', width=1)
    zerobutton.grid(row=3, column=0, columnspan=2, sticky='nswe')
    equalbutton = ttk.Button(frame, text='=', width=1)
    equalbutton.grid(row=2, column=3, rowspan=2, columnspan=2, sticky='nswe')

    for x in range(5):
        frame.grid_columnconfigure(x, weight=1)
    for y in range(4):
        frame.grid_rowconfigure(y, weight=1)

    return frame


def make_message_frame(big_frame):
    frame = ttk.Frame(big_frame)

    label = ttk.Label(frame, text="This is a very important message.")
    label.place(relx=0.5, rely=0.3, anchor='center')
    button = ttk.Button(frame, text="OK")
    button.place(relx=0.5, rely=0.8, anchor='center')

    return frame


def main():
    root = tkinter.Tk()
    big_frame = ttk.Frame(root)
    big_frame.pack(fill='both', expand=True)

    calculator = make_calculator_frame(big_frame)
    message = make_message_frame(big_frame)
    statusbar = ttk.Label(big_frame, text="This is a status bar.",
                          relief='sunken')

    statusbar.pack(side='bottom', fill='x')
    calculator.pack(side='left', fill='y')
    message.pack(side='left', fill='both', expand=True)

    root.title("Useless GUI")
    root.geometry('450x200')
    root.minsize(400, 100)
    root.mainloop()


if __name__ == '__main__':
    main()
