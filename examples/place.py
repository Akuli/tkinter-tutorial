import tkinter as tk


root = tk.Tk()

label = tk.Label(root, text="This is a very important message.")
label.place(relx=0.5, rely=0.3, anchor='center')
button = tk.Button(root, text="OK", command=root.destroy)
button.place(relx=0.5, rely=0.8, anchor='center')

root.title("Important Message")
root.geometry('250x150')
root.mainloop()
