import threading
import time
import tkinter as tk


# in a real program, we would have some other blocking thing than
# time.sleep and we would use after callbacks if we really want to sleep
def blocking_function():
    print("blocking function starts")
    time.sleep(1)
    print("blocking function ends")


def start_new_thread():
    thread = threading.Thread(target=blocking_function)
    thread.start()


root = tk.Tk()
button = tk.Button(root, text="Start the blocking function",
                   command=start_new_thread)
button.pack()
root.mainloop()
