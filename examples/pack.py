import tkinter as tk


root = tk.Tk()

button = tk.Button(root, text="This stretches")
label = tk.Label(root, text="This doesn't stretch")
statusbar = tk.Label(root, text="This is a status bar", relief='sunken')

statusbar.pack(side='bottom', fill='x')
button.pack(side='left', fill='both', expand=True)
label.pack(side='left')

root.title("Pack Test")
root.geometry('300x150')
root.mainloop()
