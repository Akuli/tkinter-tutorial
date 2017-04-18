import time
import tkinter as tk

def ok_callback():
    print("hello")

def stupid_callback():
    time.sleep(5)

root = tk.Tk()
button1 = tk.Button(root, text="This is OK", command=ok_callback)
button1.pack()
button2 = tk.Button(root, text="This sucks", command=stupid_callback)
button2.pack()
root.mainloop()
