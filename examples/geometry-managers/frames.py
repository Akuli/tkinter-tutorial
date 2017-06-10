import tkinter as tk


def make_calculator_frame(root):
    frame = tk.Frame(root)

    rows = [
        ['7', '8', '9', '*', '/'],
        ['4', '5', '6', '+', '-'],
        ['1', '2', '3', None, None],
        [None, None, '.', None, None],
    ]

    for y, row in enumerate(rows):
        for x, character in enumerate(row):
            if character is not None:
                button = tk.Button(frame, text=character)
                button.grid(row=y, column=x, sticky='nswe')

    zerobutton = tk.Button(frame, text='0')
    zerobutton.grid(row=3, column=0, columnspan=2, sticky='nswe')
    equalbutton = tk.Button(frame, text='=')
    equalbutton.grid(row=2, column=3, rowspan=2, columnspan=2, sticky='nswe')

    for x in range(5):
        frame.grid_columnconfigure(x, weight=1)
    for y in range(4):
        frame.grid_rowconfigure(y, weight=1)

    return frame


def make_message_frame(root):
    frame = tk.Frame(root)

    label = tk.Label(frame, text="This is a very important message.")
    label.place(relx=0.5, rely=0.3, anchor='center')
    button = tk.Button(frame, text="OK")
    button.place(relx=0.5, rely=0.8, anchor='center')

    return frame


def main():
    root = tk.Tk()

    calculator = make_calculator_frame(root)
    message = make_message_frame(root)
    statusbar = tk.Label(root, text="This is a status bar.", relief='sunken')

    statusbar.pack(side='bottom', fill='x')
    calculator.pack(side='left', fill='y')
    message.pack(side='left', fill='both', expand=True)

    root.title("Useless GUI")
    root.geometry('450x200')
    root.minsize(400, 100)
    root.mainloop()


if __name__ == '__main__':
    main()
