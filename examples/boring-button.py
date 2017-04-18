import tkinter as tk


root = tk.Tk()

label = tk.Label(root, text="This is a button test.")
label.pack()
button = tk.Button(root, text="Click me!")
button.pack()

root.title("Button Test")
root.geometry('200x100')
root.minsize(150, 50)
root.mainloop()
