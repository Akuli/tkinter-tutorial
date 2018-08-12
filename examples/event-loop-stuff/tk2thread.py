import queue
import threading
import time
import tkinter
from tkinter import ttk

the_queue = queue.Queue()


def thread_target():
    while True:
        message = the_queue.get()
        if message is None:
            print("thread_target: got None, exiting...")
            return

        print("thread_target: doing something with", message, "...")
        time.sleep(1)
        print("thread_target: ready for another message")


def on_click():
    the_queue.put("hello")


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

ttk.Button(big_frame, text="Click me", command=on_click).pack()
threading.Thread(target=thread_target).start()
root.mainloop()

# we get here when the user has closed the window, let's stop the thread
the_queue.put(None)
