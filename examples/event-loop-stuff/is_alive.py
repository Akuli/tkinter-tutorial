import threading
import time
import tkinter
from tkinter import ttk, messagebox


def do_slow_stuff():
    for i in range(1, 5):
        print(i, '...')
        time.sleep(1)
    print('done!')


def check_if_ready(thread):
    print('check')
    if thread.is_alive():
        # not ready yet, run the check again soon
        root.after(200, check_if_ready, thread)
    else:
        messagebox.showinfo("Ready", "I'm ready!")


def start_doing_slow_stuff():
    thread = threading.Thread(target=do_slow_stuff)
    thread.start()
    root.after(200, check_if_ready, thread)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

ttk.Button(big_frame, text="Start", command=start_doing_slow_stuff).pack()
root.mainloop()
