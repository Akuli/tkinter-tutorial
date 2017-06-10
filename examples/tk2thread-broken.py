import queue
import threading
import time
import tkinter as tk

the_queue = queue.Queue()


def after_callback():
    the_queue.put("hello")


def thread_target():
    while True:
        message = the_queue.get()
        print("thread_target: doing something with", message, "...")
        time.sleep(1)
        print("thread_target: ready for another message")


def on_click():
    the_queue.put("hello")


root = tk.Tk()
tk.Button(root, text="Click me", command=on_click).pack()
threading.Thread(target=thread_target).start()
root.mainloop()
