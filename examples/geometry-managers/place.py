import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text="This is a very important message.")
label.place(relx=0.5, rely=0.3, anchor='center')
button = ttk.Button(big_frame, text="OK", command=root.destroy)
button.place(relx=0.5, rely=0.8, anchor='center')

root.title("Important Message")
root.geometry('250x150')
root.mainloop()
