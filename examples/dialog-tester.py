import functools
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, colorchooser


class Demo:

    def __init__(self, root, modulename):
        self.frame = tk.LabelFrame(root, text=("tkinter." + modulename))
        self.modulename = modulename

    # this makes buttons that demonstrate messagebox functions
    # it's a bit weird but it makes this code much less repetitive
    def add_button(self, functionname, function, args=(), kwargs=None):
        # see http://stackoverflow.com/q/1132941
        if kwargs is None:
            kwargs = {}

        # the call_string will be like "messagebox.showinfo('Bla Bla', 'Bla')"
        parts = []
        for arg in args:
            parts.append(repr(arg))
        for key, value in kwargs.items():
            parts.append(key + "=" + repr(value))
        call_string = "%s.%s(%s)" % (self.modulename, functionname,
                                     ', '.join(parts))

        callback = functools.partial(self.on_click, call_string,
                                     function, args, kwargs)
        button = tk.Button(self.frame, text=functionname, command=callback)
        button.pack()

    def on_click(self, call_string, function, args, kwargs):
        print('running', call_string)
        result = function(*args, **kwargs)
        print('  it returned', repr(result))


root = tk.Tk()

msgboxdemo = Demo(root, "messagebox")
msgboxdemo.add_button(
    "showinfo", messagebox.showinfo,
    ["Important Message", "Hello World!"])
msgboxdemo.add_button(
    "showwarning", messagebox.showwarning,
    ["Warny Warning", "This may cause more problems."])
msgboxdemo.add_button(
    "showerror", messagebox.showerror,
    ["Fatal Error", "Something went wrong :("])
msgboxdemo.add_button(
    "askyesno", messagebox.askyesno,
    ["Important Question", "Do you like this?"])
msgboxdemo.add_button(
    "askyesnocancel", messagebox.askyesnocancel,
    ["Important Question", "Do you like this?"])
msgboxdemo.add_button(
    "askokcancel", messagebox.askokcancel,
    ["Stupid Question", "Do you really want to do this?"])
msgboxdemo.add_button(
    "askyesnocancel", messagebox.askyesnocancel,
    ["Save Changes?", "Do you want to save your changes before quitting?"])

filedialogdemo = Demo(root, "filedialog")
filedialogdemo.add_button(
    "askopenfilename", filedialog.askopenfilename,
    kwargs={'title': "Open File"})
filedialogdemo.add_button(
    "asksaveasfilename", filedialog.asksaveasfilename,
    kwargs={'title': "Save As"})

simpledialogdemo = Demo(root, "simpledialog")
simpledialogdemo.add_button(
    "askfloat", simpledialog.askfloat,
    ["Pi Question", "What's the value of pi?"])
simpledialogdemo.add_button(
    "askinteger", simpledialog.askinteger,
    ["Computer Question", "How many computers do you have?"])
simpledialogdemo.add_button(
    "askstring", simpledialog.askstring,
    ["Editor Question", "What is your favorite editor?"])

colorchooserdemo = Demo(root, "colorchooser")
colorchooserdemo.add_button(
    "askcolor", colorchooser.askcolor,
    kwargs={'title': "Choose a Color"})

msgboxdemo.frame.grid(row=0, column=0, rowspan=3)
filedialogdemo.frame.grid(row=0, column=1)
simpledialogdemo.frame.grid(row=1, column=1)
colorchooserdemo.frame.grid(row=2, column=1)

root.title("Dialog Tester")
root.resizable(False, False)
root.mainloop()
